#!/usr/bin/env python3

from w1thermsensor import W1ThermSensor
from gpiozero import LightSensor
from time import sleep

tempSensor = W1ThermSensor()
lightSensor = LightSensor(18, charge_time_limit=0.05)

while True:

    temperature = tempSensor.get_temperature(W1ThermSensor.DEGREES_F)

    light = lightSensor.value

    print ('Light: %0.2f, Temperature %0.2f' % (light, temperature))

    sleep(1)
