import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,0)
state=0

time.sleep(1)
while True:
	time.sleep(.1)
	print state
	if GPIO.input(16) == GPIO.LOW:
		state+=1
		if state==1:
			GPIO.output(17,1)
		elif state==3:
			GPIO.output(17,0)
		elif state==5:
			state=0

