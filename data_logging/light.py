#!/usr/bin/env python

from gpiozero import LightSensor
from time import sleep

ldr = LightSensor(18)

while True:

    print("Light value: ", ldr.value)

    sleep(1)
