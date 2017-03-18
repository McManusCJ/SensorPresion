import spidev
import time
import Adafruit_DHT as ada

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


print "| Hum. | Temp. | Volt. | Val D. |"
for x in range(5):
	r = ada.read(sensor_type,18)
	if (r[0])!= None:
		print "| "+str((r[0]))+" | ",
	if (r[1])!= None:
       		print str((r[1]))+" | ",
	V1=(rByte(0)*3.3/4096)
	print str(V1)+"  |  ",
	
print str( tempo/10)+"    |",


 


