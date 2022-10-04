#!/usr/bin/python3
import datetime, time

def fetchtemp():
	with open("/sys/class/thermal/thermal_zone0/temp", 'r') as file:
		temp = int(file.read()[0:5])/1000
		return str(temp)

with open("/home/pi/LearningPython/plottemp.dat", 'a') as f:
	f.write(datetime.datetime.today().strftime("%H:%M") + ' ' + fetchtemp() + '\n')
