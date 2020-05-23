#!/usr/bin/python

import os
from sense_hat import SenseHat


sense = SenseHat()

temp1 = sense.get_temperature()
temp2 = sense.get_temperature_from_pressure()


os.system("vcgencmd measure_temp")
os.system("vcgencmd measure_volts")
os.system("vcgencmd measure_clock arm")
print(str(temp1), str(temp2))
