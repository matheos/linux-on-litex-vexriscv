# DAPHNE
DAPHNE (Detector Electronic for Acquiring Photons from Neutrinos) is an instrumentation module for the PDS (Photon Detection System) at DUNE experiment in FERMILAB. DAPHNE is designed to digitize the analog signals coming from the Photon Detection Sensors of the Single Phase in the Cold Electronics side of the TPC. DAPHNE is the first instrumentation module after the TPC interface, on the warm side. 

> **Note:** Tested on Debian 10, and the xc7a200t-fbg676-3 package with the pinout presented by the hardware team. 

## Intro:
In this repository, we experiment running dedicated digital modules with a bare-bones [LiteX](https://github.com/enjoy-digital/litex) as the SoC builder and special cores written in Migen (LiteADS, LiteDRAM, LiteEth).

## Main Scheme
![scheme](general.png)

## Dependencies
> **Note:** Installation must be performed in order. Vivado tool cahin must be installed in /opt/Xilinx ... and the binaries correctly added to the PATH variables.
```sh
$ sudo apt install build-essential device-tree-compiler
```
## Download
```sh
$ git clone https://github.com/matheos/daphne
$ cd daphne
```
[Migen](https://github.com/m-labs/migen)
```sh
$ sudo pip3 install migen
```
[LiteX](https://github.com/litex-hub/litex-getting-started)
```sh
$ wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py
$ chmod +x litex_setup.py
$ sudo ./litex_setup.py init install
```
[RiscV]()
```sh
$ sudo ./litex_setup.py gcc
```
## Set-up configuraion files
```sh
$ mv daphne-platforms.py litex-boards/litex_boards/platforms/daphne.py
$ mv daphne-targets.py litex-boards/litex_boards/targets/daphne.py
```
## Build
To build the bitstream of you board, run:
```sh
$ ./make.py --board=daphne --build
```


### Load the Linux images over Serial
The board support Serial loading of the Linux images and this is the only way to load them when the board does not have others communications interfaces or storage capability.

To load the Linux images over Serial, use the [lxterm](https://github.com/enjoy-digital/litex/blob/master/litex/tools/litex_term.py) terminal/tool provided by LiteX and run:
```sh
$ ls /dev/ttyUSB*
$ lxterm --images=images.json /dev/ttyUSBX --speed=2e6 --no-crc
```
The images should load and you should see Linux booting :)

> **Note**: lxterm is automatically installed with LiteX.

> **Note:** since on some boards JTAG/Serial is shared, when you will run lxterm after loading the board, the BIOS serialboot will already have timed out. You will need to press Enter, see if you have the BIOS prompt and type *reboot*.

Since loading over Serial is working for all boards, **this is the recommended way to do initial tests** even if your board has more capabilities.

### Load the Linux images over TFTP
The board can be programmed via Ethernet,  the Linux images can be loaded over TFTP. You need to copy the files in *buildroot* directory and *emulator/emulator.bin* to your TFTP root directory. The default Local IP/Remote IP are 192.168.1.50/192.168.1.100 but you can change it with the *--local-ip* and *--remote-ip* arguments.

Once the bistream is loaded, the board you try to retrieve the files on the TFTP server. If not successful or if the boot already timed out when you see the BIOS prompt, you can retry with the *netboot* command.

The images should load and you should see Linux booting :)

### Load the Linux images to SPI-Flash
For boards that have SPI Flash (and enough space on it to store the images), the Linux images can be written to
SPI Flash and directly loaded during boot.

To flash the bitstream and linux images to you board, run:
```sh
$ ./make.py --board=XXYY --flash
```

When done, the FPGA of the board should automatically reload itself from the SPI-Flash, start the BIOS, copy
the Linux images to RAM and boot :)

## Generating the Linux binaries (optional)
```sh
$ git clone http://github.com/buildroot/buildroot
$ cd buildroot
$ make BR2_EXTERNAL=../linux-on-litex-vexriscv/buildroot/ litex_vexriscv_defconfig
$ make
```
The binaries are located in *output/images/*.


