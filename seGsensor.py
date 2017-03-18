# -*- coding: utf-8 -*-
import spidev
import time
import Adafruit_DHT as ada
import os
sensor_type = 11
readings = [[],[]]

spi=spidev.SpiDev()
spi.open(0,0)

def rByte(canal):
        if((canal<0) or (canal>1)):
                return -1
        r=spi.xfer2([1,(canal+2)<<6,0])
        #El parametro es unicamente list of values, es decir una lista de valor$
        reg=((r[1]&0x0F) << 8) + (r[2])
        return reg

tempo=0
for x in range(0,9):
        tempo += rByte(0)


#VREF=3.3
VREF=5.0
PMIN = 0
PMAX = 51.98

V1=(rByte(1)*VREF/4096)
print str(V1)+",",		#voltaje
print str(tempo+1)
