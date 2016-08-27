#!/usr/bin/env python

from w1thermsensor import W1ThermSensor
from time import sleep

sensor = W1ThermSensor()

while True:

    temperature = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    print('Temperature %0.2f' % temperature)

    sleep(1)

