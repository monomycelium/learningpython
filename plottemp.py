import datetime, time

def fetchtemp():
	with open("/sys/class/thermal/thermal_zone0/temp", 'r') as file:
		temp = int(file.read()[0:5])/1000
		return str(temp)

with open("/home/pi/LearningPython/plottemp.dat", 'a') as f:
	while True:
		for x in range(20):
			f.write(datetime.datetime.today().strftime("%H:%M") + ' ' + fetchtemp() + '\n')
			time.sleep(60)
		f.truncate(0)
