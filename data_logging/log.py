#!/usr/bin/env python3

from w1thermsensor import W1ThermSensor
from gpiozero import LightSensor
from phant import Phant
from time import sleep
from keys import PHANT_PUBLIC_KEY, PHANT_PRIVATE_KEY

tempSensor = W1ThermSensor()
lightSensor = LightSensor(18, charge_time_limit=0.05)

p = Phant(PHANT_PUBLIC_KEY, 'light', 'temp', 'location', private_key=PHANT_PRIVATE_KEY)

location = 'vs'

while True:

    temperature = tempSensor.get_temperature(W1ThermSensor.DEGREES_F)

    light = lightSensor.value

    print ('Light: %0.2f, Temperature %0.2f' % (light, temperature))

    try:
        p.log(light, temperature, location)
    except:
        print ('Error sending data to the server')

    sleep(10)
