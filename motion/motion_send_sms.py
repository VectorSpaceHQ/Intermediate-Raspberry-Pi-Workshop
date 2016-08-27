#!/usr/bin/env python3

from gpiozero import MotionSensor
from time import sleep, time
from twilio.rest import TwilioRestClient
from datetime import datetime
from twilio_credentials import TWILIO_ACCOUNT, TWILIO_TOKEN, TWILIO_PHONE

to_phone = '+15558675309'
client = TwilioRestClient(TWILIO_ACCOUNT, TWILIO_TOKEN)

lastReportTime = 0

def report_motion():

    global lastReportTime

    currentTime = time()

    if currentTime - lastReportTime > 10:
        print (datetime.now(), 'Motion Detected!')
        lastReportTime = currentTime
        try:
            message = client.messages.create(to=to_phone, from_=TWILIO_PHONE, body="Motion Detected!")
        except:
            print ('Error sending message')

pir = MotionSensor(17)
pir.when_motion = report_motion

while True:
    pass
