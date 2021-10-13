#!/usr/bin/env python3

"""
Pump function to be called directly or from crontab
See `crontab` file for sample schedules, generators, and validators
Credentials are explicit as can't guarantee crontab shell env
"""

from time import sleep
import sys
import logging

#import google.cloud.logging
import RPi.GPIO as GPIO


#create logger and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#create a format, optional
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

#create file handler with path, set formatter
file_handler = logging.FileHandler('operate_pump.log')
file_handler.setFormatter(formatter)

#add handlers to logger
logger.addHandler(file_handler)


###  CREATE HANDLER TO WRITE TO GCP CLOUD LOGS  ###
#create cloud logging client
#try:
#    client = google.cloud.logging.Client.from_service_account_json(\
#        '/home/pi/keys/crane-gcp-pi-water-plants.json')
#    #Create cloud handler and set formatter
#    cloud_handler = google.cloud.logging.handlers.CloudLoggingHandler(client)
#    cloud_handler.setFormatter(formatter)
#    #add cloud handler
#    logger.addHandler(cloud_handler)
#except FileNotFoundError:
#    logger.error('Cloud logger client not established')

# Which handlers were setup?
logger.info("Handlers: %s", logger.handlers)


def operate_pump(seconds=60):
    """Setup relay and run the pump"""
    # confirm runtime argument overrides default
    logger.info("Seconds to run: %i", seconds)

    ### Establish relay pins and run pump for seconds on pin of choice ###
    # record when trial begins
    logger.info("Starting run")

    # README: See relay_test.pi for more information on the relay configuration
    # Pump is attached to relay on pin 19
    GPIO.setmode(GPIO.BCM)
    pins = [16, 20, 21, 19]
    pin = 19

    # Setup all pins regardless of use to avoid non-deterministic behavior
    # Setup pins as output and set them high (true) as they activate on low
    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)
    logger.info("GPIO setup complete")

    # Wait before activating pump
    sleep(2)


    # Turn on relay for 10 seconds then sleep
    try:
        print("watering %i seconds" % (seconds))

        GPIO.output(pin, False)
        sleep(seconds)
        GPIO.output(pin, True)

        logger.info("Done Watering")
        GPIO.cleanup()

    # Go High-True to turn off on interupt, cleanup GPIO for good measure
    except KeyboardInterrupt:
        GPIO.output(pin, True)
        GPIO.cleanup()
        logger.error("KeyboardInterrupt")


if __name__ == "__main__":
    # function is 0 and argument is 1, python3 not involved
    seconds_input = int(sys.argv[1])
    operate_pump(seconds_input)
