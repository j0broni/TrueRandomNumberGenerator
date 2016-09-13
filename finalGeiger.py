import datetime
import RPi.GPIO as GPIO
import csv

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
 
x = 1

while 1 < 2:
	if GPIO.input(12) == True:
		data = []
		now = datetime.datetime.now()
		print x,now.isoformat()
		data.append(now.isoformat())
		with open("finalOutput.csv", "a") as f:
			writer = csv.writer(f)
			writer.writerow(data)
		x = x + 1
