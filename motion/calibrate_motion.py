#!/usr/bin/env python3

from gpiozero import MotionSensor
from datetime import datetime

pir = MotionSensor(17)

while True:
    pir.wait_for_motion();
    print (datetime.now(), 'Motion Output HIGH')
    pir.wait_for_no_motion();
    print (datetime.now(), 'Motion Output LOW')
