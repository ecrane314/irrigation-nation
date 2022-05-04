#!/usr/bin/env python3

import os
from sense_hat import SenseHat

try:
    sense = SenseHat()

    temp1 = sense.get_temperature()
    temp2 = sense.get_temperature_from_pressure()
    humid = sense.get_humidity()
    pressure = sense.get_pressure()
except:
    print("Couldn't retrieve readings from SenseHat")

os.system("vcgencmd measure_temp")
os.system("vcgencmd measure_volts")
os.system("vcgencmd measure_clock arm")
os.system("vcgencmd get_throttled")

try:
    print(str(temp1), str(temp2), str(humid), str(pressure))
else:
    print('Variables not set')