#!/usr/bin/env python3

from gpiozero import MotionSensor
from time import sleep, time
from datetime import datetime

lastReportTime = 0

def report_motion():

    global lastReportTime

    currentTime = time()

    if currentTime - lastReportTime > 10:
        print (datetime.now(), 'Motion Detected!')
        lastReportTime = currentTime

pir = MotionSensor(17)
pir.when_motion = report_motion

while True:
    pass
