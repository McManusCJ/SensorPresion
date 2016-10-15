import Adafruit_DHT as ada
sensor_type = 11
x = int(raw_input("Ingrese las iteraciones: "))
readings = [[],[]]
print "| Hum. | Temp. |"
for i in range(x):
	r = ada.read(sensor_type,18)
	if (r[0])!= None:
		print "| "+str((r[0]))+" | ",
		readings[0].append(r[0])
	if (r[1])!= None:
		print str((r[1]))+" |"
		readings[1].append(r[1])
print "-----------------"
print "Averages (H|T):",
for m in readings:
	print sum(m)/len(m),

 
