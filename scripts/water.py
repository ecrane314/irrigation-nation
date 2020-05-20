# Initial inspiration included this web front and pi backend
# https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc

# External module imp
import RPi.GPIO as GPIO
import datetime
import time

init = False

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

def get_last_watered():
    try:
        f = open("last_watered", "r")
        return f.readline()
    except:
        return "NEVER!"
      
def get_status(pin = 8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 5, pump_pin = 7, water_sensor_pin = 8):
    consecutive_water_count = 0
    init_output(pump_pin)
    print("Here we go! Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            wet = get_status(pin = water_sensor_pin) == 0
            if not wet:
                if consecutive_water_count < 5:
                    pump_on(pump_pin, 1)
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI

def pump_on(pump_pin = 7, delay = 1):
    init_output(pump_pin)
    f = open("last_watered", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)


#PASTED THIS IN, ADAPT TO WRITE LOGS
#SERVICE ACCOUNT, 
# [START logging_write_log_entry]
def write_entry(logger_name):
    """Writes log entries to the given logger."""
    logging_client = logging.Client()

    # This log can be found in the Cloud Logging console under 'Custom Logs'.
    logger = logging_client.logger(logger_name)

    # Make a simple text log
    logger.log_text('Hello, world!')

    # Simple text log with severity.
    logger.log_text('Goodbye, world!', severity='ERROR')

    # Struct log. The struct can be any JSON-serializable dictionary.
    logger.log_struct({
        'name': 'King Arthur',
        'quest': 'Find the Holy Grail',
        'favorite_color': 'Blue'
    })

    print('Wrote logs to {}.'.format(logger.name))
# [END logging_write_log_entry]
