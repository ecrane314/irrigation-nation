#!/usr/bin/env python3

# run the pump, setup to be run from cron
# https://crontab-generator.org/
# 0 8,14 * * * /usr/bin/python3 /home/pi/pi-water-plants/pump_test.py > /home/pi/water.out
# This runs twice a day, at 8am and 2pm, per linux date command.
# crontab -e to edit your crontab

"""Pump function to be called from crontab"""
#TODO import sys  sys.argv[0] etc ;  use for crontab

#FOR LIGHTS

# imports
import time
import sys
import RPi.GPIO as GPIO


def activate_lights(seconds=30):
    """Establish relay pins and run pump for seconds on pin of choice"""
    # record when trial begins
    print("Starting run at: " + str(time.localtime()))

    # README: See relay_test.pi for more information on the relay configuration
    # This is a 10 second test for the relay-attached pump on pin 19
    GPIO.setmode(GPIO.BCM)
    pins = [16, 20, 21, 19]
    pin = 20
    #seconds = 20   // now a param

    # Setup all pins regardless of use to avoid non-deterministic behavior
    # setup pins as output and set them high (true) since they activate on low
    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)
    print("GPIO setup complete")



    # Turn on relay for 10 seconds then sleep
    try:
        print("running %s seconds" % (seconds))

        GPIO.output(pin, False)
        time.sleep(seconds)
        GPIO.output(pin, True)

        print("done at: " + str(time.localtime()))
        print("==============================")
        GPIO.cleanup()

    # Go high to turn off on interupt or exit
    # cleanup the GPIO for good measure
    except:
        GPIO.output(pin, True)
        GPIO.cleanup()
        print("Exception at: " + str(time.localtime()))


if __name__ == "__main__":
    seconds = int(sys.argv[1])
    print("seconds is: %i" % seconds)
    activate_lights(seconds)
