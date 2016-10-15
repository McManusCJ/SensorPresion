import Adafruit_DHT as ada
sensor_type = 11
x = int(raw_input("Ingrese las iteraciones:"))
for i in range(x):	
	print "Hum: "+str(ada.read(sensor_type,18)[0]),
	print "Temp: "+str(ada.read(sensor_type,18)[1])


