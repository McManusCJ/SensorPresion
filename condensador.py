#!/usr/bin/env python

import pigpio,sys,getopt

pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)
try:
	opcion = getopt.getopt(sys.argv,"TF")
except getopt.GetoptError:
	print "comando incorrecto"
print opcion
if opcion[1][1]== "T":
	pi.write(17,1)
elif opcion[1][1] == "F":
	pi.write(17,0)
pi.stop()
