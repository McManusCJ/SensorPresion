#!/usr/bin/python
#!/dev/spidev<bus>.<device>

"""Programa por Bruce Nolasco et al.
"""
import spidev
import time

DEBUG = 0

spi=spidev.SpiDev()
spi.open(0,0)

def rByte(canal):
	if((canal<0) or (canal>1)):
		return -1
	r=spi.xfer2([1,(canal+2)<<6,0])  
	#El parametro es unicamente list of values, es decir una lista de valores en forma de arreglo"""
	reg=((r[1]&0x0F) << 8) + (r[2])
	return reg

tempo=0
for x in range(0,9):
	tempo += rByte(0)

V1=(rByte(0)*3.3/4096)
Ve=V1*3.3/3.3			# Voltaje de entrada

print "Valor Decimal", tempo/10
print ""
print "Divisor de Voltaje: "+str(V1) 
print ""
print ""
