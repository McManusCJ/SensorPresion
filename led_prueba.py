#!/usr/bin/env python
#LED.py
 
import time
import pigpio
pi = pigpio.pi()
 
pi.set_mode (17, pigpio.OUTPUT) #Ponemos el pin 17 como salida
pi.write(17,1)
time.sleep(5) 
#pi.set_servo_pulsewidth (17, 1300) #Iniciamos pulsos cada 1.3 segundos para encender el LED
 
pi.stop() #Terminamos el programa.
