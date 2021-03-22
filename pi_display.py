#!/usr/bin/env python3
from sense_hat import SenseHat

##https://pythonhosted.org/sense-hat/api/#environmental-sensors


def display_hello():
    #Hello, World!
    sense.show_message("Hello!", back_colour=[50,0,0])

def display_humidity():
    humidity = sense.get_humidity()
    sense.show_message("hum:")
    sense.show_message(str(int(humidity)))

def display_temp():
    temp = sense.get_temperature()
    sense.show_message("temp:")
    sense.show_message(str(int(temp)))


if __name__=="__main__":
    sense = SenseHat()
    #pi rotated upside down on my desk
    sense.set_rotation(180)
    
    display_hello()
    display_humidity()
    display_temp()
