# run the pump, setup to be run from cron
# https://crontab-generator.org/
# 0 8,14 * * * /usr/bin/python3 /home/pi/pi-water-plants/pump_test.py > /home/pi/water.out
# This runs twice a day, at 8am and 2pm, per linux date command.
# crontab -e to edit your crontab


#TODO import sys  sys.argv[0] etc ;  use for crontab

# import GPIO and time
import RPi.GPIO as GPIO
from sense_hat import SenseHat
import time


def pump_test():
    # record when trial begins
    print("Starting run at: " + str(time.localtime()))

    # README: See relay_test.pi for more information on the relay configuration
    # This is a 10 second test for the relay-attached pump on pin 19
    GPIO.setmode(GPIO.BCM)
    PINS=[16,20,21,19]
    PIN=19
    SECONDS=10

    # Setup all pins regardless of use to avoid non-deterministic behavior
    # setup pins as output and set them high (true) since they activate on low
    for i in PINS:
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,True)
    print("GPIO setup complete")


    # Prepare sense hat display
    sense = SenseHat()
    print("sleeping")
    sense.show_message("sleeping")
    time.sleep(2)


    # Turn on relay for 10 seconds then sleep
    try:
        #TODO make this non-magic, add SECONDS with formatting
        print("go-10")
        sense.show_message("go-10")

        GPIO.output(PIN,False)
        time.sleep(SECONDS)
        GPIO.output(PIN,True)

        print("done at: " + str(time.localtime()))
        sense.show_message("done")
        # would running cleanup before the message interfere with the display?
        GPIO.cleanup()

    # Go high to turn off on interupt or exit
    # cleanup the GPIO for good measure
    except:
        GPIO.output(PIN,True)
        GPIO.cleanup()
        print("Exception at: " + str(time.localtime()))


if __name__=="__main__":
    pump_test()
