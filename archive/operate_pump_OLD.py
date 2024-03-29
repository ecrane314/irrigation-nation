#!/usr/bin/env python3

# run the pump, setup to be run from cron
# https://crontab-generator.org/
# 0 8,14 * * * /usr/bin/python3 /home/pi/pi-water-plants/pump_test.py > /home/pi/water.out
# This runs twice a day, at 8am and 2pm, per linux date command.
# crontab -e to edit your crontab

"""Pump function to be called from crontab"""
#TODO Separate sense_hat logic in case hardware failure, wont interfere

# imports
import time
import sys
import RPi.GPIO as GPIO
#from sense_hat import SenseHat


def operate_pump(seconds=60):

    # confirm runtime argument overrides default
    print("Seconds to run: %i" % seconds)

    """Establish relay pins and run pump for seconds on pin of choice"""
    # record when trial begins
    print("Starting run at: " + str(time.localtime()))

    # README: See relay_test.pi for more information on the relay configuration
    # This is a 10 second test for the relay-attached pump on pin 19
    GPIO.setmode(GPIO.BCM)
    pins = [16, 20, 21, 19]
    pin = 19
    #seconds = 20   // now a param

    # Setup all pins regardless of use to avoid non-deterministic behavior
    # setup pins as output and set them high (true) since they activate on low
    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)
    print("GPIO setup complete")


    # Prepare sense hat display
   # sense = SenseHat()
    print("sleeping")
   # sense.show_message("sleeping")
    time.sleep(2)


    # Turn on relay for 10 seconds then sleep
    try:
        print("watering %i seconds" % (seconds))
     #   sense.show_message("go-%i" % (seconds))

        GPIO.output(pin, False)
        time.sleep(seconds)
        GPIO.output(pin, True)

        print("done at: " + str(time.localtime()))
    #    sense.show_message("done")
        # would running cleanup before the message interfere with the display?
        GPIO.cleanup()

    # Go high to turn off on interupt or exit
    # cleanup the GPIO for good measure
    except:
        GPIO.output(pin, True)
        GPIO.cleanup()
        print("Exception at: " + str(time.localtime()))


if __name__ == "__main__":
    # function is 0 and argument is 1, python3 not involved
    seconds = int(sys.argv[1])
    print("seconds is: %i" % seconds)
    operate_pump(seconds)
