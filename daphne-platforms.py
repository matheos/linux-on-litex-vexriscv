h# This file is Copyright (c) 2015-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# License: BSD

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [

    ("afedat0", 0, Pins("AE25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 1, Pins("AE26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 2, Pins("AC22"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 3, Pins("AC23"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 4, Pins("AF24"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 5, Pins("AF25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 6, Pins("AD25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 7, Pins("AD26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 8, Pins("AE23"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 9, Pins("AF23"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 10, Pins("AD23"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 11, Pins("AD24"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 12, Pins("AD21"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 13, Pins("AE21"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 14, Pins("AF19"), IOStandard("DIFF_SSTL18_II")),
    ("afedat0", 15, Pins("AF20"), IOStandard("DIFF_SSTL18_II")),

    ("afedat1", 0, Pins("AE18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 1, Pins("AF18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 2, Pins("Y18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 3, Pins("AA18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 4, Pins("AE17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 5, Pins("AF17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 6, Pins("AA17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 7, Pins("AB17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 8, Pins("AC17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 9, Pins("AD17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 10, Pins("Y16"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 11, Pins("Y17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 12, Pins("AB16"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 13, Pins("AC16"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 14, Pins("Y15"), IOStandard("DIFF_SSTL18_II")),
    ("afedat1", 15, Pins("AA15"), IOStandard("DIFF_SSTL18_II")),

    ("afedat2", 0, Pins("U25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 1, Pins("U26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 2, Pins("V26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 3, Pins("W26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 4, Pins("AB26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 5, Pins("AC26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 6, Pins("W25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 7, Pins("Y26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 8, Pins("Y25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 9, Pins("AA25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 10, Pins("V24"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 11, Pins("W24"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 12, Pins("AA24"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 13, Pins("AB25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 14, Pins("AA22"), IOStandard("DIFF_SSTL18_II")),
    ("afedat2", 15, Pins("AA23"), IOStandard("DIFF_SSTL18_II")),

    ("afedat3", 0, Pins("W20"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 1, Pins("Y20"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 2, Pins("T19"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 3, Pins("U19"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 4, Pins("V19"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 5, Pins("W19"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 6, Pins("V18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 7, Pins("W18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 8, Pins("T14"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 9, Pins("T15"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 10, Pins("T17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 11, Pins("T18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 12, Pins("U15"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 13, Pins("U16"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 14, Pins("U14"), IOStandard("DIFF_SSTL18_II")),
    ("afedat3", 15, Pins("V14"), IOStandard("DIFF_SSTL18_II")),

    ("afedat4", 0, Pins("P15"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 1, Pins("P16"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 2, Pins("N16"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 3, Pins("N17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 4, Pins("R16"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 5, Pins("R17"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 6, Pins("P18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 7, Pins("N18"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 8, Pins("K25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 9, Pins("K26"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 10, Pins("M20"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 11, Pins("L20"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 12, Pins("L24"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 13, Pins("L25"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 14, Pins("M24"), IOStandard("DIFF_SSTL18_II")),
    ("afedat4", 15, Pins("M25"), IOStandard("DIFF_SSTL18_II")),

    ("spi_afe", 0,
        Subsignal("sclk", Pins("K15"), IOStandard("LVCMOS33")),
        Subsignal("miso", Pins("J14"), IOStandard("LVCMOS33")),
        Subsignal("mosi", Pins("J16"), IOStandard("LVCMOS33")),
        Subsignal("cs_n", 0 ,Pins("K18"), IOStandard("LVCMOS33")),
        Subsignal("cs_n", 1 ,Pins("K17"), IOStandard("LVCMOS33")),
        Subsignal("cs_n", 2 ,Pins("M15"), IOStandard("LVCMOS33")),
        Subsignal("cs_n", 3 ,Pins("H18"), IOStandard("LVCMOS33")),
    ),

    ("afe_cfg", 0,
        Subsignal("fclkp",Pins("AB21"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("fclkm",Pins("AC21"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkp",Pins("AA20"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkm",Pins("AB20"), IOStandard("DIFF_SSTL18_II")),
    ),

    ("afe_cfg", 1,
        Subsignal("fclkp",Pins("AC19"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("fclkm",Pins("AD19"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkp",Pins("AA19"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkm",Pins("AB19"), IOStandard("DIFF_SSTL18_II")),
    ),

    ("afe_cfg", 2,
        Subsignal("fclkp",Pins("Y22"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("fclkm",Pins("Y23"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkp",Pins("U22"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkm",Pins("V22"), IOStandard("DIFF_SSTL18_II")),
    ),

    ("afe_cfg", 3,
        Subsignal("fclkp",Pins("W21"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("fclkm",Pins("Y21"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkp",Pins("U21"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dclkm",Pins("V21"), IOStandard("DIFF_SSTL18_II")),
    ),

    ("muxen", 0, Pins("N16"), IOStandard("LVCMOS15")),
    ("muxen", 1, Pins("N17"), IOStandard("LVCMOS15")),
    ("muxen", 2, Pins("R16"), IOStandard("LVCMOS15")),
    ("muxen", 3, Pins("R17"), IOStandard("LVCMOS15")),
    ("muxen", 4, Pins("N19"), IOStandard("LVCMOS15")),
    ("muxen", 5, Pins("P23"), IOStandard("LVCMOS15")),
    ("muxen", 6, Pins("P24"), IOStandard("LVCMOS15")),
    ("muxen", 7, Pins("R20"), IOStandard("LVCMOS15")),
    ("muxen", 8, Pins("R21"), IOStandard("LVCMOS15")),
    ("muxen", 9, Pins("R25"), IOStandard("LVCMOS15")),
    ("refin_mux", 0, Pins("K25"), IOStandard("LVCMOS15")),
    ("ss_cfg_dat", 0, Pins("R15"), IOStandard("LVCMOS15")),
 
    
    ("gain_cs", 0, Pins("N26"), IOStandard("LVCMOS15")),
    ("bias_cs", 0, Pins("M26"), IOStandard("LVCMOS15")),

    ("offset_cfg", 0, 
        Subsignal("sclk", Pins("L22"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("sdat", Pins("M25"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("ld", Pins("M24"), IOStandard("DIFF_SSTL18_II")),
    ),

    ("offset", 0, Pins("K26"), IOStandard("LVCMOS15")),
    ("offset", 1, Pins("M20"), IOStandard("LVCMOS15")),
    ("offset", 2, Pins("L20"), IOStandard("LVCMOS15")),
    ("offset", 3, Pins("L24"), IOStandard("LVCMOS15")),
    ("offset", 4, Pins("L25"), IOStandard("LVCMOS15")),

    ("trim_cfg", 0, 
        Subsignal("sclk", Pins("T24"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("sdat", Pins("T25"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("ld", Pins("R26"), IOStandard("DIFF_SSTL18_II")),
    ),

    ("trim", 0, Pins("P26"), IOStandard("LVCMOS15")),
    ("trim", 1, Pins("T22"), IOStandard("LVCMOS15")),
    ("trim", 2, Pins("R22"), IOStandard("LVCMOS15")),
    ("trim", 3, Pins("T23"), IOStandard("LVCMOS15")),
    ("trim", 4, Pins("R23"), IOStandard("LVCMOS15")),

    ("sled", 0, Pins("AD5"), IOStandard("LVCMOS15")),
    ("sled", 1, Pins("AE5"), IOStandard("LVCMOS15")),
    ("sled", 2, Pins("V9"), IOStandard("LVCMOS15")),

    ("gpiled", 0, Pins("AF2"), IOStandard("LVCMOS15")),

    ("lemo", 0,
        Subsignal("gpi", Pins("AA4")),
        Subsignal("gpo", Pins("AB4")),
        IOStandard("LVCMOS33"),
    ),

    ("phy", 0,
        Subsignal("mdio", Pins("AB2")),
        Subsignal("mdc", Pins("AC2")),
        IOStandard("LVCMOS33"),
    ),

    ("brdy", 0,
        Subsignal("brdy0", Pins("AE3")),
        Subsignal("brdy1", Pins("AF3")),
        IOStandard("LVCMOS33"),
    ),

    ("dma", 0,
        Subsignal("en", Pins("AC3")),
        Subsignal("bsy", Pins("AD3")),
        IOStandard("LVCMOS33"),
    ),

    ("control", 0,
        Subsignal("eth_cs", Pins("AB1")),
        Subsignal("cpld_cs", Pins("AC1")),
        Subsignal("rd", Pins("Y1")),
        Subsignal("wr", Pins("AD1")),
        Subsignal("nwait", Pins("AE1")),
        Subsignal("cpld_irq", Pins("AE2")),
        IOStandard("LVCMOS33"),
    ),

    ("stm", 0,
        Subsignal("ca", Pins(
            "V1 W1 W5 W4 V3 V2 V6 W6 W3 Y3 U7 V7"),
            IOStandard("LVCMOS15")),
        Subsignal("cd", Pins("AF5 AF4 AC4 AD4 Y7 AA7 Y6 Y5" 
            "V8 W8 AA5 AB5 Y8 AA8 AB6 AC6"), 
            IOStandard("LVCMOS15")),
    ),

    ("dbg", 0, Pins("D3 C3 F3 E3 C2 B2 A3 A2"
        "C1 B1 F2 E2 E1 D1 G2 G1"), IOStandard("LVCMOS15")),


    ("clk0", 0, 
        Subsignal("clk_p", Pins("G5"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_n", Pins("F5"), IOStandard("DIFF_SSTL18_II")),
    ),

    ("clk62.5", 0, Pins("AA4"), IOStandard("LVCMOS15")),

    ("pll", 0, 
        Subsignal("pll_sclk", Pins("C18"), IOStandard("SSTL18_II")),
        Subsignal("pll_sdat", Pins("D19"), IOStandard("SSTL18_II")),
        Subsignal("pll_pdn", Pins("E20"), IOStandard("SSTL18_II")),
        Subsignal("pll_status", Pins("D20"), IOStandard("SSTL18_II")),
        Subsignal("pll_ld", Pins("E22"), IOStandard("SSTL18_II")),
    ),

    ("cdr", 0, 
        Subsignal("cdr_p", Pins("D4"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("cdr_n", Pins("C4"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("sfp_scl", Pins("B20"), IOStandard("SSTL18_II")),
        Subsignal("sfp_sda", Pins("A20"), IOStandard("SSTL18_II")),
        Subsignal("f_sfp_tx_fault", Pins("C21"), IOStandard("SSTL18_II")),
        Subsignal("f_sfp_los", Pins("B21"), IOStandard("SSTL18_II")),
        Subsignal("f_cdr_lol", Pins("B22"), IOStandard("SSTL18_II")),
        Subsignal("f_cdr_los", Pins("A22"), IOStandard("SSTL18_II")),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "T2 R2 U2 U1 P6 P5 T5 R5 U6",
            "P8 R7 R6 T8 T7"),
            IOStandard("SSTL18_II")),
        Subsignal("ba", Pins("K1 J1 L3"), IOStandard("SSTL18_II")),
        Subsignal("ras_n", Pins("H2"), IOStandard("SSTL18_II")),
        Subsignal("cas_n", Pins("M2"), IOStandard("SSTL18_II")),
        Subsignal("we_n", Pins("N3"), IOStandard("SSTL18_II")),
        Subsignal("dm", Pins("N1 M1"), IOStandard("SSTL18_II")),
        Subsignal("dq", Pins(
            "N6 N7 K5 L5 L7 M7 J3 K3"), IOStandard("SSTL18_II"),
            Misc("IN_TERM=UNTUNED_SPLIT_50")),
        Subsignal("dqs_p", Pins("M4"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("L4"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_p", Pins("R3"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_n", Pins("P3"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("cke", Pins("L2"), IOStandard("SSTL18_II")),
        Subsignal("odt", Pins("H1"), IOStandard("SSTL18_II")),
        Subsignal("cs_n", Pins("T3"), IOStandard("SSTL18_II")),
        Misc("SLEW=FAST"),
    ),

    # Verify this!!! This is CPLD Reset

     ("cpu_reset", 0, Pins("Y2"), IOStandard("LVCMOS15")),


    # Verify This!!!
    ("serial", 0,
        Subsignal("tx", Pins("D3")),
        Subsignal("rx", Pins("C3")),
        IOStandard("LVCMOS33"),
    ),

    ("sfp_csr_i2c", 0,
        Subsignal("scl", Pins("B20")),
        Subsignal("sda", Pins("A20")),
        IOStandard("LVCMOS25")),

    ("sfp_i2c", 0,
        Subsignal("tx_f", Pins("E21")),
        Subsignal("tx_d", Pins("D21")),
        Subsignal("present", Pins("C22")),
        Subsignal("rate_s", Pins("C23")),
        Subsignal("los", Pins("B25")),
        Subsignal("sda", Pins("A25")),
        Subsignal("scl", Pins("A23")),
        IOStandard("LVCMOS25")
    ),

    ("sfp_i2c", 1,
        Subsignal("tx_f", Pins("B26")),
        Subsignal("tx_d", Pins("C24")),
        Subsignal("present", Pins("B24")),
        Subsignal("rate_s", Pins("D23")),
        Subsignal("los", Pins("D24")),
        Subsignal("sda", Pins("C26")),
        Subsignal("scl", Pins("A24")),
        IOStandard("LVCMOS25")
    ),

]


# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name = "clk62.5"
    default_clk_period = 1e9/62.5e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a200t-fbg676-3", _io,  toolchain="vivado")
        self.toolchain.bitstream_commands = \
            ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
        self.toolchain.additional_commands = \
            ["write_cfgmem -force -format bin -interface spix4 -size 16 "
             "-loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")


    def create_programmer(self):
        return VivadoProgrammer(flash_part="n25q128-3.3v-spi-x1_x2_x4")

    # def do_finalize(self, fragment):
    #     XilinxPlatform.do_finalize(self, fragment)
    #     try:
    #         self.add_period_constraint(self.lookup_request("eth_clocks").rx, 1e9/125e6)
    #     except ConstraintError:
    #         pass
    def load(self):
        from litex.build.xilinx import VivadoProgrammer
        prog=VivadoProgrammer()
        prog.load_bitstream("build/top.bit")

# class Platform(XilinxPlatform):
#     default_clk_name = "clk156"
#     default_clk_period = 1e9/156.5e6

#     def __init__(self):
#         XilinxPlatform.__init__(self, "xc7a200t-fbg676-3", _io,  toolchain="vivado")
#         self.toolchain.bitstream_commands = ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
#         self.toolchain.additional_commands = ["write_cfgmem -force -format bin -interface spix4 -size 16 -loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]
#         self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 33]")
#         self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")
#         self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 35]")

#     def create_programmer(self):
#         return VivadoProgrammer()

#     def do_finalize(self, fragment):
#         XilinxPlatform.do_finalize(self, fragment)
#         try:
#             self.add_period_constraint(self.lookup_request("clk200").p, 1e9/200e6)
#         except ConstraintError:
#             pass
#         try:
#             self.add_period_constraint(self.lookup_request("eth_clocks").rx, 1e9/125e6)
#         except ConstraintError:
#             pass
#         try:
#             self.add_period_constraint(self.lookup_request("eth_clocks").tx, 1e9/125e6)
#         except ConstraintError:
#             pass
