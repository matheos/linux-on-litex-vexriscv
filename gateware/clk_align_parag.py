from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex.soc.cores.code_8b10b import Encoder, Decoder
from migen.genlib.cdc import *

from gtp_7series_init import GTPTXInit, GTPRXInit
from clock_aligner import BruteforceClockAligner

from prbs_files.tx_top import _TX
from prbs_files.rx_top import _RX


class GTPQuadPLL(Module):
    def __init__(self, refclk, refclk_freq, linerate):
        self.clk = Signal()
        self.refclk = Signal()
        self.reset = Signal()
        self.lock = Signal()
        self.config = self.compute_config(refclk_freq, linerate)

        # # #

        self.specials += \
            Instance("GTPE2_COMMON",
                # common
                i_GTREFCLK0=refclk,
                i_BGBYPASSB=1,
                i_BGMONITORENB=1,
                i_BGPDB=1,
                i_BGRCALOVRD=0b11111,
                i_RCALENB=1,

                # pll0
                p_PLL0_FBDIV=self.config["n2"],
                p_PLL0_FBDIV_45=self.config["n1"],
                p_PLL0_REFCLK_DIV=self.config["m"],
                i_PLL0LOCKEN=1,
                i_PLL0PD=0,
                i_PLL0REFCLKSEL=0b001,
                i_PLL0RESET=self.reset,
                o_PLL0LOCK=self.lock,
                o_PLL0OUTCLK=self.clk,
                o_PLL0OUTREFCLK=self.refclk,

                # pll1 (not used: power down)
                i_PLL1PD=1,
             )

    @staticmethod
    def compute_config(refclk_freq, linerate):
        for n1 in 4, 5:
            for n2 in 1, 2, 3, 4, 5:
                for m in 1, 2:
                    vco_freq = refclk_freq*(n1*n2)/m
                    if 1.6e9 <= vco_freq <= 3.3e9:
                        for d in 1, 2, 4, 8:
                            current_linerate = vco_freq*2/d
                            if current_linerate == linerate:
                                return {"n1": n1, "n2": n2, "m": m, "d": d,
                                        "vco_freq": vco_freq,
                                        "clkin": refclk_freq,
                                        "linerate": linerate}
        msg = "No config found for {:3.2f} MHz refclk / {:3.2f} Gbps linerate."
        raise ValueError(msg.format(refclk_freq/1e6, linerate/1e9))

    def __repr__(self):
        r = """
GTPQuadPLL
==============
  overview:
  ---------
       +--------------------------------------------------+
       |                                                  |
       |   +-----+  +---------------------------+ +-----+ |
       |   |     |  | Phase Frequency Detector  | |     | |
CLKIN +----> /M  +-->       Charge Pump         +-> VCO +---> CLKOUT
       |   |     |  |       Loop Filter         | |     | |
       |   +-----+  +---------------------------+ +--+--+ |
       |              ^                              |    |
       |              |    +-------+    +-------+    |    |
       |              +----+  /N2  <----+  /N1  <----+    |
       |                   +-------+    +-------+         |
       +--------------------------------------------------+
                            +-------+
                   CLKOUT +->  2/D  +-> LINERATE
                            +-------+
  config:
  -------
    CLKIN    = {clkin}MHz
    CLKOUT   = CLKIN x (N1 x N2) / M = {clkin}MHz x ({n1} x {n2}) / {m}
             = {vco_freq}GHz
    LINERATE = CLKOUT x 2 / D = {vco_freq}GHz x 2 / {d}
             = {linerate}GHz
""".format(clkin=self.config["clkin"]/1e6,
           n1=self.config["n1"],
           n2=self.config["n2"],
           m=self.config["m"],
           vco_freq=self.config["vco_freq"]/1e9,
           d=self.config["d"],
           linerate=self.config["linerate"]/1e9)
        return r


class GTP(Module):
    def __init__(self, qpll,drp_host,tx_pads, rx_pads, sys_clk_freq,
                 clock_aligner=True):
        self.tx_seldata = Signal()
        self.rx_seldata = Signal()
        self.tx_en8b10b = Signal()
        self.rx_en8b10b = Signal()
        self.enable_err_count = Signal(2)
        self.total_bit_count = Signal(32)
        self.tx_prbs_config = Signal(2)
        self.rx_prbs_config = Signal(2)
        self.global_error = Signal(32)
        self.tx_input = Signal(20)
        self.tx_mask = Signal(20)
        self.rx_mask = Signal(20)
        self.k = Signal(2)
        self.rx_ready = Signal()

        self.plllock = Signal()
        self.loopback = Signal(3)
        self.tx_polarity = Signal()
        self.rx_polarity = Signal()
        self.diffctrl = Signal(4)
        self.txprecursor = Signal(5)
        self.txpostcursor = Signal(5)
        self.checklink = Signal()
        self.linkstatus = Signal()

        self.rx_reset_host = Signal()
        self.tx_reset_host = Signal()
        self.rx_reset_ack = Signal()
        self.tx_reset_ack = Signal()
        self.rx_restart_phaseAlign = Signal()
        self.rx_phaseAlign_ack = Signal()
        self.tx_clk_freq = qpll.config["linerate"]/20

        # DRP signals

        self.drpaddr = Signal(9)
        self.drpen = Signal()
        self.drpdi = Signal(16)
        self.drprdy = Signal()
        self.drpdo = Signal(16)
        self.drpwe = Signal()

        # # # #

        tx = ClockDomainsRenamer("tx")(_TX(20,True))
        rx = ClockDomainsRenamer("rx")(_RX(20,True))
        self.submodules += tx,rx

        # TX generates RTIO clock, init must be in system domain
        tx_init = GTPTXInit(sys_clk_freq)
        # RX receives restart commands from RTIO domain
        rx_init = ClockDomainsRenamer("tx")(GTPRXInit(self.tx_clk_freq))
        self.submodules += tx_init, rx_init
        # debug
        self.tx_init = tx_init
        self.rx_init = rx_init

        # transceiver direct clock outputs
        # useful to specify clock constraints in a way palatable to Vivado
        self.txoutclk = Signal()
        self.rxoutclk = Signal()

        # control/status cdc

        self.comb += [
        tx.seldata.eq(self.tx_seldata),
        tx.en8b10b.eq(self.tx_en8b10b),
        tx.tx_prbs_config.eq(self.tx_prbs_config),
        tx.mask.eq(self.tx_mask),
        tx.k.eq(self.k),
        tx.input.eq(self.tx_input)
        ]

        self.comb += [
        rx.seldata.eq(self.rx_seldata),
        rx.en8b10b.eq(self.rx_en8b10b),
        rx.enable_err_count.eq(self.enable_err_count),
        rx.rx_prbs_config.eq(self.rx_prbs_config),
        self.global_error.eq(rx.global_error),
        self.total_bit_count.eq(rx.total_bit_count),
        rx.mask.eq(self.rx_mask),
        rx.checklink.eq(self.checklink),
        self.linkstatus.eq(rx.linkstatus)
        ]

        self.comb += [
        self.tx_reset_ack.eq(tx_init.done),
        self.rx_reset_ack.eq(rx_init.done),
        tx_init.restart.eq(self.tx_reset_host)
        ]

        self.comb += [
            self.plllock.eq(qpll.lock),
            tx_init.plllock.eq(qpll.lock),
            rx_init.plllock.eq(qpll.lock),
            qpll.reset.eq(tx_init.pllreset)
        ]

        # DRP Mux selected by rx_init

        self.comb += [
        If(rx_init.drp_mux_sel == 1,
            self.drpaddr.eq(rx_init.drpaddr),
            self.drpdi.eq(rx_init.drpdi),
            rx_init.drpdo.eq(self.drpdo),
            self.drpen.eq(rx_init.drpen),
            self.drpwe.eq(rx_init.drpwe),
            rx_init.drprdy.eq(self.drprdy)
        ).Else(
            self.drpaddr.eq(drp_host.drpaddr),
            self.drpdi.eq(drp_host.drpdi),
            drp_host.drpdo.eq(self.drpdo),
            self.drpen.eq(drp_host.drpen),
            self.drpwe.eq(drp_host.drpwe),
            drp_host.drprdy.eq(self.drprdy)

        )]

        assert qpll.config["linerate"] < 6.6e9
        # rxcdr_cfgs = {
        #      1 : 0x0001107FE206021041010,
        #      2 : 0x0001107FE206021081010,
        #      4 : 0x0001107FE086021101010,
        #      8 : 0x0001107FE086021101010
        # }
        rxcdr_cfgs = {
            1 : 0x0000107FE406001041010,
            2 : 0x0000107FE206001041010,
            4 : 0x0000107FE106001041010,
            8 : 0x0000107FE086001041010
        }

        rxphaligndone = Signal()
        self.specials += \
            Instance("GTPE2_CHANNEL",
                i_GTRESETSEL=0,
                i_RESETOVRD=0,
                p_SIM_RESET_SPEEDUP="FALSE",

                # DRP
                i_DRPADDR=self.drpaddr,
                i_DRPCLK=ClockSignal("tx"),
                i_DRPDI=self.drpdi,
                o_DRPDO=self.drpdo,
                i_DRPEN=self.drpen,
                o_DRPRDY=self.drprdy,
                i_DRPWE=self.drpwe,

                # PMA Attributes
                # p_PMA_RSV=0x333,
                # p_PMA_RSV2=0x2040,
                # p_PMA_RSV3=0,
                # p_PMA_RSV4=0,
                # p_RX_BIAS_CFG=0b0000111100110011,
                # p_RX_CM_SEL=0b01,
                # p_RX_CM_TRIM=0b1010,
                # p_RX_OS_CFG=0b10000000,
                # p_RXLPM_IPCM_CFG=1,
                i_RXOOBRESET=0,
                i_RXELECIDLEMODE=0b11,
                # i_RXOSINTCFG=0b0010,
                # i_RXOSINTEN=1,

                # Power-Down Attributes
                # p_PD_TRANS_TIME_FROM_P2=0x3c,
                # p_PD_TRANS_TIME_NONE_P2=0x3c,
                # p_PD_TRANS_TIME_TO_P2=0x64,

                # QPLL
                i_PLL0CLK=qpll.clk,
                i_PLL0REFCLK=qpll.refclk,

                #TX clock
                o_TXOUTCLK=self.txoutclk,
                p_TXOUT_DIV=qpll.config["d"],
                i_TXRATE=0b000,
                i_TXSYSCLKSEL=0b00,
                i_TXOUTCLKSEL=0b11,

                # TX Startup/Reset
                i_GTTXRESET=tx_init.gttxreset,
                i_RXPD=Cat(rx_init.gtrxpd, rx_init.gtrxpd),
                i_TXPMARESET=0,
                i_TXPCSRESET=0,
                o_TXRESETDONE=tx_init.txresetdone,
                i_TXSYNCMODE=0,
                i_TXPHDLYRESET=0,
                i_TXDLYBYPASS=0,
                i_TXSYNCALLIN=0,
                i_TXSYNCIN=0,
                i_TXDLYSRESET=tx_init.txdlysreset,
                o_TXDLYSRESETDONE=tx_init.txdlysresetdone,
                i_TXPHINIT=tx_init.txphinit,
                o_TXPHINITDONE=tx_init.txphinitdone,
                i_TXPHALIGNEN=1,
                i_TXPHALIGN=tx_init.txphalign,
                o_TXPHALIGNDONE=tx_init.txphaligndone,
                i_TXDLYEN=tx_init.txdlyen,
                i_TXUSERRDY=tx_init.txuserrdy,

                # TX Buffer Attributes
                p_TXBUF_EN="FALSE",
                p_TX_XCLK_SEL="TXUSR",
                p_TXSYNC_MULTILANE=0,
                p_TXSYNC_SKIP_DA=0,
                p_TXSYNC_OVRD=1,

                # TX data
                p_TX_DATA_WIDTH=20,
                i_TXCHARDISPMODE=Cat(tx.txdata[9],tx.txdata[19]),
                i_TXCHARDISPVAL=Cat(tx.txdata[8],tx.txdata[18]),
                i_TXDATA=Cat(tx.txdata[:8], tx.txdata[10:18]),
                i_TXUSRCLK=ClockSignal("tx"),
                i_TXUSRCLK2=ClockSignal("tx"),

                # TX electrical
                i_TXBUFDIFFCTRL=0b100,
                i_TXDIFFCTRL=self.diffctrl,
                i_TXELECIDLE=0,
                i_TXINHIBIT=0,
                i_TXPOSTCURSOR=self.txpostcursor,
                i_TXPRECURSOR=self.txprecursor,

                # Internal Loopback
                i_LOOPBACK=self.loopback,

                # RX Startup/Reset
                i_GTRXRESET=rx_init.gtrxreset,
                o_RXRESETDONE=rx_init.rxresetdone,
                i_RXDLYSRESET=rx_init.rxdlysreset,
                o_RXDLYSRESETDONE=rx_init.rxdlysresetdone,
                o_RXPHALIGNDONE=rxphaligndone,
                i_RXSYNCALLIN=rxphaligndone,
                i_RXUSERRDY=rx_init.rxuserrdy,
                i_RXCDRRESET=0,
                i_RXCDRFREQRESET=0,
                i_RXPMARESET=0,
                i_RXLPMRESET=0,
                i_EYESCANRESET=0,
                i_RXPCSRESET=0,
                i_RXBUFRESET=0,
                i_RXSYNCIN=0,
                i_RXSYNCMODE=1,
                p_RXSYNC_MULTILANE=0,
                p_RXSYNC_OVRD=0,
                o_RXSYNCDONE=rx_init.rxsyncdone,
                p_RXPMARESET_TIME=0b11,
                o_RXPMARESETDONE=rx_init.rxpmaresetdone,

                # RX clock
                p_RX_CLK25_DIV=5,
                p_TX_CLK25_DIV=5,
                p_RX_XCLK_SEL="RXUSR",
                i_RXRATE=0b000,
                p_RXOUT_DIV=qpll.config["d"],
                i_RXSYSCLKSEL=0b00,
                i_RXOUTCLKSEL=0b010,
                o_RXOUTCLK=self.rxoutclk,
                i_RXUSRCLK=ClockSignal("rx"),
                i_RXUSRCLK2=ClockSignal("rx"),
                p_RXCDR_CFG=rxcdr_cfgs[qpll.config["d"]],
                p_RXPI_CFG1=1,
                p_RXPI_CFG2=1,

                # RX Clock Correction Attributes
                p_CLK_CORRECT_USE="FALSE",

                # RX data
                p_RXBUF_EN="FALSE",
                p_RXDLY_CFG=0x001f,
                p_RXDLY_LCFG=0x030,
                p_RXPHDLY_CFG=0x084020,
                p_RXPH_CFG=0xc00002,
                p_RX_DATA_WIDTH=20,
                i_RXCOMMADETEN=1,
                i_RXDLYBYPASS=0,
                i_RXDDIEN=1,
                o_RXDISPERR=Cat(rx.rxdata[9], rx.rxdata[19]),
                o_RXCHARISK=Cat(rx.rxdata[8], rx.rxdata[18]),
                o_RXDATA=Cat(rx.rxdata[:8], rx.rxdata[10:18]),

                # Polarity
                i_TXPOLARITY=self.tx_polarity,
                i_RXPOLARITY=self.rx_polarity,

                # Pads
                i_GTPRXP=rx_pads.p,
                i_GTPRXN=rx_pads.n,
                o_GTPTXP=tx_pads.p,
                o_GTPTXN=tx_pads.n
            )


        
        # tx clocking
        self.clock_domains.cd_tx = ClockDomain()
        self.specials += Instance("BUFG", i_I=self.txoutclk, o_O=self.cd_tx.clk)

        #rx clocking
        self.clock_domains.cd_rx = ClockDomain()
        self.specials += Instance("BUFG", i_I=self.rxoutclk, o_O=self.cd_rx.clk)

        if clock_aligner:
            clock_aligner = BruteforceClockAligner(0b0101111100, self.tx_clk_freq, check_period=10e-3)
            self.submodules += clock_aligner
            self.comb += [
                clock_aligner.rxdata.eq(rx.rxdata),
                rx_init.restart.eq(clock_aligner.restart | self.rx_reset_host),
                clock_aligner.rx_restart_phaseAlign.eq(self.rx_restart_phaseAlign),
                self.rx_phaseAlign_ack.eq(clock_aligner.rx_phaseAlign_ack)
            ]