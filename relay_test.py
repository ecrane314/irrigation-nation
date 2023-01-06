#!/usr/bin/env python3

# import GPIO and time
import RPi.GPIO as GPIO
import time

# Which scheme and pins are you using?
# I'm using SenseHat, so I avoid these six https://pinout.xyz/pinout/sense_hat 
# and avoid board pins 27 and 28 as they are hat identification pins
# set GPIO numbering mode and define output pins
# GPIO.BCM or GPIO.BOARD are valid numbering modes.
# Using 16,19,20,21 for physical board pins 36,35,38,40
GPIO.setmode(GPIO.BCM)
PINS=[16,19,20,21]

# setup pins as output and set them high since they activate on low
for i in PINS:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,True)

print("sleeping")
time.sleep(1)

# cycle those relays
try:
    k=0
    while True:
        k+=1
        print("cycle %s begins" % k)
        for j in PINS:
            GPIO.output(j,False)
            time.sleep(1)
            GPIO.output(j,True)

# cleanup the GPIO for good measure
except:
    GPIO.cleanup()
