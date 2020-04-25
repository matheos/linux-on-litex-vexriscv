from migen import *
from litex.soc.interconnect.csr import *
from litex.soc.cores.spi import SPIMaster

from gateware.pwm import PWM


class ClassicLed(gpio.GPIOOut):
    def __init__(self, pads):
        gpio.GPIOOut.__init__(self, pads)


class RGBLed(Module, AutoCSR):
    def __init__(self, pads):
        nleds = len(pads.r)

        # # #

        for n in range(nleds):
            for c in "rgb":
                setattr(self.submodules, c+str(n), PWM(getattr(pads, c)[n]))


class afe_spi(Module, AutoCSR):
    def __init__(self, pads):
    	
        spi_pads = Record([("cs_n", 1), ("clk", 1), ("mosi", 1)])
        self.submodules.spi = SPIMaster(spi_pads, 8, div=16, cpha=0)
        self.comb += [
            pads.sclk.eq(spi_pads.clk),
            pads.sdin.eq(spi_pads.mosi)
        ]

class afe_data(Module,AutoCSR):
	def __init__(self,pads):
		npads=len(pads.data)
        for n in range(npads):
            for c in "rgb":
                setattr(self.submodules, c+str(n), PWM(getattr(pads, c)[n]))

        self.submodules.gpio = GPIOOut(Cat(pads.res, pads.dc, pads.vbat, pads.vdd))