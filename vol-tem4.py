# -*- coding: utf-8 -*-
import spidev
import time
import Adafruit_DHT as ada
import os
#import pigpio
#pi = pigpio.pi()
#pi.set_mode (12, pigpio.OUTPUT)
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

V1=(rByte(0)*VREF/4096)
V2=(rByte(1)*VREF/4096)

#V1=(((V1/VREF)-0.1)/0.8)*(PMAX-PMIN)+PMIN

r=[None,None]
while (r[0])==None and (r[1])==None:
	print "No funciono"
	r = ada.read(sensor_type,18)
	if (r[0])!= None:
		print str((r[0]))+",",	#humedad
	if (r[1])!= None:
      		print str((r[1]))+",",	#temperatura
print str(V1)+",",		#voltaje
print str(V2)+",",              #voltaje 2
print str(tempo/10)+",",	#decimal del voltaje
print time.time()		#tiempo epoch

#presion = "sensor.presion "+str(V1)+" `date +%s`"
#os.system('echo \"'+presion+'\" | nc 172.16.2.15 2003')

#nivel = "sensor.nivel "+str(V2)+" `date +%s`"
#os.system('echo \"'+nivel+'\" | nc 172.16.2.15 2003')

#humedad = "sensor.humedad "+str(r[0])+" `date +%s`" 
#os.system('echo \"'+humedad+'\" | nc 172.16.2.15 2003')

#temperatura = "sensor.temperatura "+str(r[1])+" `date +%s`" 
#os.system('echo \"'+temperatura+'\" | nc 172.16.2.15 2003')

#enviar='echo \"'+presion+'\" | nc 172.16.2.15 2003'
#print(enviar)

#os.system("echo 'enviar' >> prueba.txt")

