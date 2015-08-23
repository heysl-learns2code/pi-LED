#!/usr/bin/env python
# light running back and forth
import RPi.GPIO as GPIO
import time
 
pins = [11, 12, 13, 15, 16, 18, 22, 7]

def setup():
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode is output
        GPIO.output(pin, GPIO.HIGH) # Set all pins to high(+3.3V) to off led
 
def loop(interval, reverse):
    if reverse == False:
        for pin in pins:
            GPIO.output(pin, GPIO.LOW) 
            time.sleep(interval)
            GPIO.output(pin, GPIO.HIGH)

    else:
        for pin in reversed(pins):
            GPIO.output(pin, GPIO.LOW) 
            time.sleep(interval)
            GPIO.output(pin, GPIO.HIGH)
 
def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)    # turn off all leds
    GPIO.cleanup()                     # Release resource
 
if __name__ == '__main__':     # Program start from here
    setup()
    try:
        t = True
        while True:
            loop(0.035, t)
            t = not(t)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()