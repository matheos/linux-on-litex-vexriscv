# This file is Copyright (c) 2015-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# License: BSD

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("afedat0", 0, Pins("AE25"), IOStandard("LVCMOS15")),
    ("afedat0", 1, Pins("AE26"), IOStandard("LVCMOS15")),
    ("afedat0", 2, Pins("AC22"), IOStandard("LVCMOS15")),
    ("afedat0", 3, Pins("AC23"), IOStandard("LVCMOS15")),
    ("afedat0", 4, Pins("AF24"), IOStandard("LVCMOS15")),
    ("afedat0", 5, Pins("AF25"), IOStandard("LVCMOS15")),
    ("afedat0", 6, Pins("AD25"), IOStandard("LVCMOS15")),
    ("afedat0", 7, Pins("AD26"), IOStandard("LVCMOS15")),
    ("afedat0", 8, Pins("AE23"), IOStandard("LVCMOS15")),
    ("afedat0", 9, Pins("AF23"), IOStandard("LVCMOS15")),
    ("afedat0", 10, Pins("AD23"), IOStandard("LVCMOS15")),
    ("afedat0", 11, Pins("AD24"), IOStandard("LVCMOS15")),
    ("afedat0", 12, Pins("AD21"), IOStandard("LVCMOS15")),
    ("afedat0", 13, Pins("AE21"), IOStandard("LVCMOS15")),
    ("afedat0", 14, Pins("AF19"), IOStandard("LVCMOS15")),
    ("afedat0", 15, Pins("AF20"), IOStandard("LVCMOS15")),

    ("afedat1", 0, Pins("AE18"), IOStandard("LVCMOS15")),
    ("afedat1", 1, Pins("AF18"), IOStandard("LVCMOS15")),
    ("afedat1", 2, Pins("Y18"), IOStandard("LVCMOS15")),
    ("afedat1", 3, Pins("AA18"), IOStandard("LVCMOS15")),
    ("afedat1", 4, Pins("AE17"), IOStandard("LVCMOS15")),
    ("afedat1", 5, Pins("AF17"), IOStandard("LVCMOS15")),
    ("afedat1", 6, Pins("AA17"), IOStandard("LVCMOS15")),
    ("afedat1", 7, Pins("AB17"), IOStandard("LVCMOS15")),
    ("afedat1", 8, Pins("AC17"), IOStandard("LVCMOS15")),
    ("afedat1", 9, Pins("AD17"), IOStandard("LVCMOS15")),
    ("afedat1", 10, Pins("Y16"), IOStandard("LVCMOS15")),
    ("afedat1", 11, Pins("Y17"), IOStandard("LVCMOS15")),
    ("afedat1", 12, Pins("AB16"), IOStandard("LVCMOS15")),
    ("afedat1", 13, Pins("AC16"), IOStandard("LVCMOS15")),
    ("afedat1", 14, Pins("Y15"), IOStandard("LVCMOS15")),
    ("afedat1", 15, Pins("AA15"), IOStandard("LVCMOS15")),

    ("afedat2", 0, Pins("U25"), IOStandard("LVCMOS15")),
    ("afedat2", 1, Pins("U26"), IOStandard("LVCMOS15")),
    ("afedat2", 2, Pins("V26"), IOStandard("LVCMOS15")),
    ("afedat2", 3, Pins("W26"), IOStandard("LVCMOS15")),
    ("afedat2", 4, Pins("AB26"), IOStandard("LVCMOS15")),
    ("afedat2", 5, Pins("AC26"), IOStandard("LVCMOS15")),
    ("afedat2", 6, Pins("W25"), IOStandard("LVCMOS15")),
    ("afedat2", 7, Pins("Y26"), IOStandard("LVCMOS15")),
    ("afedat2", 8, Pins("Y25"), IOStandard("LVCMOS15")),
    ("afedat2", 9, Pins("AA25"), IOStandard("LVCMOS15")),
    ("afedat2", 10, Pins("V24"), IOStandard("LVCMOS15")),
    ("afedat2", 11, Pins("W24"), IOStandard("LVCMOS15")),
    ("afedat2", 12, Pins("AA24"), IOStandard("LVCMOS15")),
    ("afedat2", 13, Pins("AB25"), IOStandard("LVCMOS15")),
    ("afedat2", 14, Pins("AA22"), IOStandard("LVCMOS15")),
    ("afedat2", 15, Pins("AA23"), IOStandard("LVCMOS15")),


    ("afedat3", 0, Pins("W20"), IOStandard("LVCMOS15")),
    ("afedat3", 1, Pins("Y20"), IOStandard("LVCMOS15")),
    ("afedat3", 2, Pins("T19"), IOStandard("LVCMOS15")),
    ("afedat3", 3, Pins("U19"), IOStandard("LVCMOS15")),
    ("afedat3", 4, Pins("V19"), IOStandard("LVCMOS15")),
    ("afedat3", 5, Pins("W19"), IOStandard("LVCMOS15")),
    ("afedat3", 6, Pins("V18"), IOStandard("LVCMOS15")),
    ("afedat3", 7, Pins("W18"), IOStandard("LVCMOS15")),
    ("afedat3", 8, Pins("T14"), IOStandard("LVCMOS15")),
    ("afedat3", 9, Pins("T15"), IOStandard("LVCMOS15")),
    ("afedat3", 10, Pins("T17"), IOStandard("LVCMOS15")),
    ("afedat3", 11, Pins("T18"), IOStandard("LVCMOS15")),
    ("afedat3", 12, Pins("U15"), IOStandard("LVCMOS15")),
    ("afedat3", 13, Pins("U16"), IOStandard("LVCMOS15")),
    ("afedat3", 14, Pins("U14"), IOStandard("LVCMOS15")),
    ("afedat3", 15, Pins("V14"), IOStandard("LVCMOS15")),

    ("afedat4", 0, Pins("P15"), IOStandard("LVCMOS15")),
    ("afedat4", 1, Pins("P16"), IOStandard("LVCMOS15")),
    ("afedat4", 2, Pins("N16"), IOStandard("LVCMOS15")),
    ("afedat4", 3, Pins("N17"), IOStandard("LVCMOS15")),
    ("afedat4", 4, Pins("R16"), IOStandard("LVCMOS15")),
    ("afedat4", 5, Pins("R17"), IOStandard("LVCMOS15")),
    ("afedat4", 6, Pins("P18"), IOStandard("LVCMOS15")),
    ("afedat4", 7, Pins("N18"), IOStandard("LVCMOS15")),
    ("afedat4", 8, Pins("K25"), IOStandard("LVCMOS15")),
    ("afedat4", 9, Pins("K26"), IOStandard("LVCMOS15")),
    ("afedat4", 10, Pins("M20"), IOStandard("LVCMOS15")),
    ("afedat4", 11, Pins("L20"), IOStandard("LVCMOS15")),
    ("afedat4", 12, Pins("L24"), IOStandard("LVCMOS15")),
    ("afedat4", 13, Pins("L25"), IOStandard("LVCMOS15")),
    ("afedat4", 14, Pins("M24"), IOStandard("LVCMOS15")),
    ("afedat4", 15, Pins("M25"), IOStandard("LVCMOS15")),


    #("vadj", 0, Pins("w22, W12"), IOStandard("LVCMOS25")),

    ("clk100", 0, Pins("N21"), IOStandard("LVCMOS15")),

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

    # ("eth_clocks", 0,
    #     Subsignal("tx", Pins("G1")),
    #     Subsignal("rx", Pins("G2")),
    #     IOStandard("LVCMOS25")
    # ),
    # ("eth", 0,
    #     Subsignal("rst_n", Pins("U7"), IOStandard("LVCMOS33")),
    #     Subsignal("int_n", Pins("Y14")),
    #     Subsignal("mdio", Pins("Y16")),
    #     Subsignal("mdc", Pins("AA16")),
    #     Subsignal("rx_ctl", Pins("W10")),
    #     Subsignal("rx_data", Pins("AB16 AA15 AB15 AB11")),
    #     Subsignal("tx_ctl", Pins("V10")),
    #     Subsignal("tx_data", Pins("Y12 W12 W11 Y11")),
    #     IOStandard("LVCMOS25")
    # ),
]


# Platform -----------------------------------------------------------------------------------------

# class Platform(XilinxPlatform):
#     default_clk_name = "clk100"
#     default_clk_period = 1e9/100e6

#     def __init__(self):
#         XilinxPlatform.__init__(self, "xc7a200t-fbg676-3", _io,  toolchain="vivado")
#         self.toolchain.bitstream_commands = \
#             ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
#         self.toolchain.additional_commands = \
#             ["write_cfgmem -force -format bin -interface spix4 -size 16 "
#              "-loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]
#         self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")


#     def create_programmer(self):
#         return VivadoProgrammer(flash_part="n25q128-3.3v-spi-x1_x2_x4")

#     # def do_finalize(self, fragment):
#     #     XilinxPlatform.do_finalize(self, fragment)
#     #     try:
#     #         self.add_period_constraint(self.lookup_request("eth_clocks").rx, 1e9/125e6)
#     #     except ConstraintError:
#     #         pass
#     def load(self):
#         from litex.build.xilinx import VivadoProgrammer
#         prog=VivadoProgrammer()
#         prog.load_bitstream("build/top.bit")

class Platform(XilinxPlatform):
    default_clk_name = "clk156"
    default_clk_period = 1e9/156.5e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a200t-fbg676-3", _io,  toolchain="vivado")
        self.toolchain.bitstream_commands = ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
        self.toolchain.additional_commands = ["write_cfgmem -force -format bin -interface spix4 -size 16 -loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 33]")
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 35]")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        try:
            self.add_period_constraint(self.lookup_request("clk200").p, 1e9/200e6)
        except ConstraintError:
            pass
        try:
            self.add_period_constraint(self.lookup_request("eth_clocks").rx, 1e9/125e6)
        except ConstraintError:
            pass
        try:
            self.add_period_constraint(self.lookup_request("eth_clocks").tx, 1e9/125e6)
        except ConstraintError:
            pass
