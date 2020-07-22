#!/usr/bin/env python3

import sys
import argparse
import os

from litex.soc.integration.builder import Builder

from soc_linux import SoCLinux, video_resolutions

kB = 1024

# Board definition----------------------------------------------------------------------------------

class Board:
    soc_kwargs = {}
    def __init__(self, soc_cls=None, soc_capabilities={}, bitstream_ext=""):
        self.soc_cls          = soc_cls
        self.soc_capabilities = soc_capabilities
        self.bitstream_ext    = bitstream_ext

    def load(self, filename):
        prog = self.platform.create_programmer()
        prog.load_bitstream(filename)

    def flash(self):
        raise NotImplementedError

# Arty support -------------------------------------------------------------------------------------

class Arty(Board):
    SPIFLASH_PAGE_SIZE    = 256
    SPIFLASH_SECTOR_SIZE  = 64*kB
    SPIFLASH_DUMMY_CYCLES = 11
    def __init__(self):
        from litex_boards.targets import arty
        Board.__init__(self, arty.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
            # Storage
            "spiflash",
            "sdcard",
            # GPIOs
            "leds",
            "rgb_led",
            "switches",
            # Buses
            "spi",
            "i2c",
            # Monitoring
            "xadc",
            # 7-Series specific
            "mmcm",
            "icap_bitstream",
        }, bitstream_ext=".bit")

class ArtyA7(Arty):
    SPIFLASH_DUMMY_CYCLES = 7

class ArtyS7(Arty):
    def __init__(self):
        from litex_boards.targets import arty_s7
        Board.__init__(self, arty_s7.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            # Storage
            "spiflash",
            "sdcard",
            # GPIOs
            "leds",
            "rgb_led",
            "switches",
            # Buses
            "spi",
            "i2c",
            # Monitoring
            "xadc",
            # 7-Series specific
            "mmcm",
            "icap_bitstream",
        }, bitstream_ext=".bit")

# NeTV2 support ------------------------------------------------------------------------------------

class NeTV2(Board):
    SPIFLASH_PAGE_SIZE    = 256
    SPIFLASH_SECTOR_SIZE  = 64*kB
    SPIFLASH_DUMMY_CYCLES = 11
    def __init__(self):
        from litex_boards.targets import netv2
        Board.__init__(self, netv2.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
            # Storage
            "spiflash",
            "spisdcard",
            # GPIOs
            "leds",
            # Video
            "framebuffer",
            # Monitoring
            "xadc",
        }, bitstream_ext=".bit")

# Genesys2 support ---------------------------------------------------------------------------------

class Genesys2(Board):
    def __init__(self):
        from litex_boards.targets import genesys2
        Board.__init__(self, genesys2.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
            # Storage
            "spisdcard",
        }, bitstream_ext=".bit")

# KC705 support ---------------------------------------------------------------------------------

class KC705(Board):
    soc_kwargs = {"uart_baudrate": 500e3} # 1Mbauds not supported by CP210x.
    def __init__(self):
        from litex_boards.targets import kc705
        Board.__init__(self, kc705.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
            # Storage
            "spisdcard",
            # GPIOs
            "leds",
            # Monitoring
            "xadc",
        }, bitstream_ext=".bit")

# KCU105 support -----------------------------------------------------------------------------------

class KCU105(Board):
    soc_kwargs = {"uart_baudrate": 115.2e3} # FIXME: understand why not working with more.
    def __init__(self):
        from litex_boards.targets import kcu105
        Board.__init__(self, kcu105.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
            # Storage
            "spisdcard",
        }, bitstream_ext=".bit")

# ZCU104 support -----------------------------------------------------------------------------------

class ZCU104(Board):
    def __init__(self):
        from litex_boards.targets import zcu104
        Board.__init__(self, zcu104.BaseSoC, soc_capabilities={
            # Communication
            "serial",
        }, bitstream_ext=".bit")

# Nexys4DDR support --------------------------------------------------------------------------------

class Nexys4DDR(Board):
    def __init__(self):
        from litex_boards.targets import nexys4ddr
        Board.__init__(self, nexys4ddr.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
            # Storage
            "spisdcard",
        }, bitstream_ext=".bit")

# NexysVideo support -------------------------------------------------------------------------------

class NexysVideo(Board):
    def __init__(self):
        from litex_boards.targets import nexys_video
        Board.__init__(self, nexys_video.BaseSoC, soc_capabilities={
            # Communication
            "usb_fifo",
            # Storage
            "spisdcard",
            # Video
            "framebuffer",
        }, bitstream_ext=".bit")

# MiniSpartan6 support -----------------------------------------------------------------------------

class MiniSpartan6(Board):
    soc_kwargs = {
        "sdram_sys2x":  True, # Use HalfRate SDRAM PHY.
        "l2_size":      2048, # Reduce l2_size (Not enough blockrams).
    }
    def __init__(self):
        from litex_boards.targets import minispartan6
        Board.__init__(self, minispartan6.BaseSoC, soc_capabilities={
            # Communication
            "usb_fifo",
            # Storage
            "spisdcard",
        }, bitstream_ext=".bit")

# Pipistrello support ------------------------------------------------------------------------------

class Pipistrello(Board):
    def __init__(self):
        from litex_boards.targets import pipistrello
        Board.__init__(self, pipistrello.BaseSoC, soc_capabilities={
            # Communication
            "serial",
        }, bitstream_ext=".bit")

# Versa ECP5 support -------------------------------------------------------------------------------

class VersaECP5(Board):
    SPIFLASH_PAGE_SIZE    = 256
    SPIFLASH_SECTOR_SIZE  = 64*kB
    SPIFLASH_DUMMY_CYCLES = 11
    def __init__(self):
        from litex_boards.targets import versa_ecp5
        Board.__init__(self, versa_ecp5.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
            # Storage
            "spiflash",
        }, bitstream_ext=".svf")

# ULX3S support ------------------------------------------------------------------------------------

class ULX3S(Board):
    def __init__(self):
        from litex_boards.targets import ulx3s
        Board.__init__(self, ulx3s.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            # Storage
            "spisdcard",
        }, bitstream_ext=".svf")

# HADBadge support ---------------------------------------------------------------------------------

class HADBadge(Board):
    SPIFLASH_PAGE_SIZE    = 256
    SPIFLASH_SECTOR_SIZE  = 64*kB
    SPIFLASH_DUMMY_CYCLES = 8
    def __init__(self):
        from litex_boards.targets import hadbadge
        Board.__init__(self, hadbadge.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            # Storage
            "spiflash",
        }, bitstream_ext=".bit")

    def load(self, filename):
        os.system("dfu-util --alt 2 --download {} --reset".format(filename))

# OrangeCrab support -------------------------------------------------------------------------------

class OrangeCrab(Board):
    soc_kwargs = {
        "sys_clk_freq": 64e6,          # Increase sys_clk_freq to 64MHz (48MHz default).
        "l2_size":      2048,          # Reduce l2_size (Not enough blockrams).
		"integrated_rom_size": 0xa000, # Reduce integrated_rom_size.
    }
    def __init__(self):
        from litex_boards.targets import orangecrab
        os.system("git clone https://github.com/gregdavill/valentyusb -b hw_cdc_eptri")
        sys.path.append("valentyusb") # FIXME: do proper install of ValentyUSB.
        Board.__init__(self, orangecrab.BaseSoC, soc_capabilities={
            # Communication
            "usb_acm",
            # Storage
            "spisdcard",
        }, bitstream_ext=".bit")

# Cam Link 4K support ------------------------------------------------------------------------------

class CamLink4K(Board):
    def __init__(self):
        from litex_boards.targets import camlink_4k
        Board.__init__(self, camlink_4k.BaseSoC, soc_capabilities={
            # Communication
            "serial",
        }, bitstream_ext=".bit")

    def load(self, filename):
        os.system("camlink configure {}".format(filename))

# TrellisBoard support -----------------------------------------------------------------------------

class TrellisBoard(Board):
    def __init__(self):
        from litex_boards.targets import trellisboard
        Board.__init__(self, trellisboard.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            # Storage
            "sdcard",
        }, bitstream_ext=".svf")

# ECPIX5 support -----------------------------------------------------------------------------------

class ECPIX5(Board):
    def __init__(self):
        from litex_boards.targets import ecpix5
        Board.__init__(self, ecpix5.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            "ethernet",
        }, bitstream_ext=".svf")

# De10Lite support ---------------------------------------------------------------------------------

class De10Lite(Board):
    def __init__(self):
        from litex_boards.targets import de10lite
        Board.__init__(self, de10lite.BaseSoC, soc_capabilities={
            # Communication
            "serial",
        }, bitstream_ext=".sof")

# De10Nano support ----------------------------------------------------------------------------------

class De10Nano(Board):
    soc_kwargs = {"with_mister_sdram": True} # Add MiSTer SDRAM extension.
    def __init__(self):
        from litex_boards.targets import de10nano
        Board.__init__(self, de10nano.BaseSoC, soc_capabilities={
            # Communication
            "serial",
            # Storage
            "spisdcard",
            # GPIOs
            "leds",
            "switches",
        }, bitstream_ext=".sof")

# De0Nano support ----------------------------------------------------------------------------------

class De0Nano(Board):
    soc_kwargs = {"l2_size": 2048} # Reduce l2_size (Not enough blockrams).
    def __init__(self):
        from litex_boards.targets import de0nano
        Board.__init__(self, de0nano.BaseSoC, soc_capabilities={
            # Communication
            "serial",
        }, bitstream_ext=".sof")

# Main ---------------------------------------------------------------------------------------------

supported_boards = {
    # Xilinx
    "arty":         Arty,
    "arty_a7":      ArtyA7,
    "arty_s7":      ArtyS7,
    "netv2":        NeTV2,
    "genesys2":     Genesys2,
    "kc705":        KC705,
    "kcu105":       KCU105,
    "zcu104":       ZCU104,
    "nexys4ddr":    Nexys4DDR,
    "nexys_video":  NexysVideo,
    "minispartan6": MiniSpartan6,
    "pipistrello":  Pipistrello,

    # Lattice
    "versa_ecp5":   VersaECP5,
    "ulx3s":        ULX3S,
    "hadbadge":     HADBadge,
    "orangecrab":   OrangeCrab,
    "camlink_4k":   CamLink4K,
    "trellisboard": TrellisBoard,
    "ecpix5":       ECPIX5,

    # Altera/Intel
    "de0nano":      De0Nano,
    "de10lite":     De10Lite,
    "de10nano":     De10Nano,
}

def main():
    description = "Linux on LiteX-VexRiscv\n\n"
    description += "Available boards:\n"
    for name in supported_boards.keys():
        description += "- " + name + "\n"
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--board",          required=True,            help="FPGA board")
    parser.add_argument("--build",          action="store_true",      help="Build bitstream")
    parser.add_argument("--load",           action="store_true",      help="Load bitstream (to SRAM)")
    parser.add_argument("--flash",          action="store_true",      help="Flash bitstream/images (to SPI Flash)")
    parser.add_argument("--doc",            action="store_true",      help="Build documentation")
    parser.add_argument("--local-ip",       default="192.168.1.50",   help="Local IP address")
    parser.add_argument("--remote-ip",      default="192.168.1.100",  help="Remote IP address of TFTP server")
    parser.add_argument("--spi-data-width", type=int, default=8,      help="SPI data width (maximum transfered bits per xfer)")
    parser.add_argument("--spi-clk-freq",   type=int, default=1e6,    help="SPI clock frequency")
    parser.add_argument("--video",          default="1920x1080_60Hz", help="Video configuration")
    args = parser.parse_args()

    # Board(s) selection ---------------------------------------------------------------------------
    if args.board == "all":
        board_names = list(supported_boards.keys())
    else:
        args.board = args.board.lower()
        args.board = args.board.replace(" ", "_")
        board_names = [args.board]

    # Board(s) iteration ---------------------------------------------------------------------------
    for board_name in board_names:
        board = supported_boards[board_name]()

        # SoC parameters ---------------------------------------------------------------------------
        board.soc_kwargs.update(integrated_rom_size=0x10000)
        if "usb_fifo" in board.soc_capabilities:
            board.soc_kwargs.update(uart_name="usb_fifo")
        if "usb_acm" in board.soc_capabilities:
            board.soc_kwargs.update(uart_name="usb_acm")
        if "ethernet" in board.soc_capabilities:
            board.soc_kwargs.update(with_ethernet=True)

        # SoC creation -----------------------------------------------------------------------------
        soc = SoCLinux(board.soc_cls, **board.soc_kwargs)
        board.platform = soc.platform

        # SoC peripherals --------------------------------------------------------------------------
        if board_name in ["arty", "arty_a7"]:
            from litex_boards.platforms.arty import _sdcard_pmod_io
            board.platform.add_extension(_sdcard_pmod_io)

        if "mmcm" in board.soc_capabilities:
            soc.add_mmcm(2)
        if "spiflash" in board.soc_capabilities:
            soc.add_spi_flash(dummy_cycles=board.SPIFLASH_DUMMY_CYCLES)
            soc.add_constant("SPIFLASH_PAGE_SIZE", board.SPIFLASH_PAGE_SIZE)
            soc.add_constant("SPIFLASH_SECTOR_SIZE", board.SPIFLASH_SECTOR_SIZE)
        if "spisdcard" in board.soc_capabilities:
            soc.add_spi_sdcard()
        if "sdcard" in board.soc_capabilities:
            soc.add_sdcard()
        if "ethernet" in board.soc_capabilities:
            soc.configure_ethernet(local_ip=args.local_ip, remote_ip=args.remote_ip)
        #if "leds" in board.soc_capabilities:
        #    soc.add_leds()
        if "rgb_led" in board.soc_capabilities:
            soc.add_rgb_led()
        if "switches" in board.soc_capabilities:
            soc.add_switches()
        if "spi" in board.soc_capabilities:
            soc.add_spi(args.spi_data_width, args.spi_clk_freq)
        if "i2c" in board.soc_capabilities:
            soc.add_i2c()
        if "xadc" in board.soc_capabilities:
            soc.add_xadc()
        if "framebuffer" in board.soc_capabilities:
            assert args.video in video_resolutions.keys(), "Unsupported video resolution"
            video_settings = video_resolutions[args.video]
            soc.add_framebuffer(video_settings)
        if "icap_bitstream" in board.soc_capabilities:
            soc.add_icap_bitstream()
        soc.configure_boot()

        # Build ------------------------------------------------------------------------------------
        build_dir = os.path.join("build", board_name)
        builder   = Builder(soc, output_dir=build_dir, csr_json=os.path.join(build_dir, "csr.json"), bios_options=["TERM_MINI"])
        builder.build(build_name="top", run=args.build)

        # DTS --------------------------------------------------------------------------------------
        soc.generate_dts(board_name)
        soc.compile_dts(board_name)

        # Machine Mode Emulator --------------------------------------------------------------------
        soc.compile_emulator(board_name)

        # Load FPGA bitstream ----------------------------------------------------------------------
        if args.load:
            board.load(filename=os.path.join(build_dir, "gateware", "top" + board.bitstream_ext))

        # Generate SoC documentation ---------------------------------------------------------------
        if args.doc:
            soc.generate_doc(board_name)

if __name__ == "__main__":
    main()
