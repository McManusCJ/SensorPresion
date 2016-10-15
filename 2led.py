from gpiozero import LED
from time import sleep
pink=LED(17)
prender = int(input("Quieres que me prenda? 1 para si: "))
if prender == 1:
	pink.on()
	sleep(3)
	pink.off()
else:
	print "Bye"
	pink.on()
	sleep(0.5)
	pink.off()
