#!/usr/bin/env python

import pigpio,sys,getopt,MySQLdb

try:
	db = MySQLdb.connect("172.16.2.15", "raspberry", "coyote", "control_con")
except getopt.GetoptError:
	print "Error"

pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)

cursor = db.cursor()
cursor.execute("SELECT * FROM CONDENSADOR")
estado = cursor.fetchone()

if estado == FALSE:
	pi.write(17,1)
elif estado == TRUE:
	pi.write(17,0)
pi.stop()
