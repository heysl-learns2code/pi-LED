from RPi import GPIO as GPIO
import time

SER = 11 	#define state of current pin -- HIGH = 1, LOW = 0
RCLK = 12	#output current pin states   -- output on HIGH, wait on LOW
SRCLK = 13	#shift to next pin 			 -- HIGH = shift
#SRCLR = 15 	#clear shifts

def setup():
	""" set up GPIO pins """
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(SER, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
#	GPIO.setup(SRCLR, GPIO.OUT)
	GPIO.output(SER, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)
#	GPIO.output(SRCLR, GPIO.LOW)
	print "Setup completed, all pins on LOW"

def HC595_go():
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)
	print "Output is now set."

def HC595_input(liste):
	""" set register values on HC595 """
	for lst in liste:
		for i in lst:
			GPIO.output(SER, i) #set state of current pin
			GPIO.output(SRCLK, GPIO.HIGH)
			time.sleep(0.001)
			GPIO.output(SRCLK, GPIO.LOW)
		HC595_go()
		time.sleep(0.125)


def destroy():
#	GPIO.output(SRCLR, GPIO.HIGH)
#	time.sleep(0.001)
#	GPIO.output(SRCLR, GPIO.LOW)
#	HC595_go()
	GPIO.cleanup()
	print "All pins cleared."




