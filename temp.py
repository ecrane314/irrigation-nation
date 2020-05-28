#!/usr/bin/python

import os
from sense_hat import SenseHat


sense = SenseHat()

temp1 = sense.get_temperature()
temp2 = sense.get_temperature_from_pressure()
humid = sense.get_humidity()
pressure = sense.get_pressure()

os.system("vcgencmd measure_temp")
os.system("vcgencmd measure_volts")
os.system("vcgencmd measure_clock arm")
os.system("vcgencmd get_throttled")
print(str(temp1), str(temp2), str(humid), str(pressure))
