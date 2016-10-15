from gpiozero import LED
from time import sleep
led = LED(17)
print 'Reaction.py ingrese frecuencia y repeticiones: /n'
frec = float(input("frec:"))
rep = int(input("repeticiones:"))
for i in range(rep):
	led.on()
	sleep(1/frec)
	led.off()
	sleep(1/frec)
