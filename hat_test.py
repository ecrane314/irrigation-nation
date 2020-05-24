"""
Test for all SenseHat functions to ensure wiring is correct when I detach it
from the Pi and connect it via wires described on pinout here:
https://pinout.xyz/pinout/sense_hat

Will test each function in their order in the API:
https://pythonhosted.org/sense-hat/api/
"""

import time
from sense_hat import SenseHat

sense = SenseHat()

try:
    sense.set_imu_config(True, True, True)
except:
    print("No IMU Detected!")

try:
    while True:
        #LED Matrix Test
        sense.show_message("Hello, world!", text_colour=[50, 50, 50])

        #Environmental sensors
        humid = sense.get_humidity()
        temp = sense.get_temperature_from_humidity()
        pressure = sense.get_pressure()
        temp2 = sense.get_temperature_from_pressure()

        print("humidity: " + str(humid))
        print("temp: "+ str(sense.temp))
        print("pressure: "+ str(pressure))
        print("temp2: "+ str(temp2))

        #IMU Sensor (inertial measurement unit)
        heading = sense.get_compass() #magneto
        gyro_only = sense.get_gyroscope() #gyro
        accel_only = sense.get_accelerometer() #accel
        print("Heading: %s" % heading)
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

        #Joystick
        # Skipping joystick because that's a pain.

        # wait, then repeat
        time.sleep(1)
except:
    sense.clear()
    print("exiting, clearing screen")
