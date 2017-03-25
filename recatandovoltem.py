import spidev
import time
import Adafruit_DHT as ada
from datetime import datetime
actual = datetime.now()
sensor_type = 11
readings = [[],[],[]]
registro = open("registros.txt","a")

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

V1=(rByte(0)*3.3/4096)

for x in range(5):
	r = ada.read(sensor_type,18)
	if (r[0])!= None:
		readings[0].append(r[0])
		print ", "+str((r[0]))+" , ",
	if (r[1])!= None:
		readings[1].append(r[1])
       		print str((r[1]))+" , "
print str(V1)+"  ,  "
print str( tempo/10)+"    |"
print actual


 


#!/usr/bin/python
import spidev
import Adafruit_DHT as ada
import MySQLdb

sensor_type = 11
readings = [[],[],[]]
#registro = open("/var/registros.txt","a")

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

V1=(rByte(0)*3.3/4096)

for x in range(5):
	r = ada.read(sensor_type,18)
	if (r[0])!= None:
		readings[0].append(r[0])
	if (r[1])!= None:
		readings[1].append(r[1])

data=[0 for x in range(3)]
data[0]=float(sum(readings[0]))/len(readings[0])
data[1]=float(sum(readings[1]))/len(readings[1])
data[2]= float("{0:.4f}".format(V1))

#data = ["localhost", "icnsensor", "coyote", "SENSOR"]
conn = MySQLdb.connect(passwd="coyote",db="SENSOR")
conn.query()
c = conn.cursor()
query = "INSERT INTO DATOS(DAT_TEMP,DAT_HUM,DAT_VOLT) VALUES("+str(data[1])+"','"+str(data[2])+"','"+str(data[0])+"');"
c.execute(query)
cursor.close()
conn.close()

#registro_actual = " Hum : "+str(data[0])+" Temp : "+str(data[1])+" Volt : "+str(data[2])+"\n"
#registro.write(registro_actual)
 
 


import spidev
import time
import Adafruit_DHT as ada
from datetime import datetime
import mysql.connector
actual = datetime.now()
sensor_type = 11
readings = [[],[],[]]
registro = open("registros.txt","a")

conexion = mysql.connector.connect(user="root", password="coyote", database="SENSOR")

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

V1=(rByte(0)*3.3/4096)

for x in range(5):
	r = ada.read(sensor_type,18)
	if (r[0])!= None:
		readings[0].append(r[0])
	if (r[1])!= None:
		readings[1].append(r[1])

data=[0 for x in range(3)]
data[0]=float(sum(readings[0]))/len(readings[0])
data[1]=float(sum(readings[1]))/len(readings[1])
data[2]= float("{0:.4f}".format(V1))

registro_actual = str(actual)+" Hum : "+str(data[0])+" Temp : "+str(data[1])+" Volt : "+str(data[2])+"\n"
print registro_actual
registro.write(registro_actual)
conexioc 
 


