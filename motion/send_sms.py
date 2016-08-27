#!/usr/bin/env python3

from twilio.rest import TwilioRestClient
from twilio_credentials import TWILIO_ACCOUNT, TWILIO_TOKEN, TWILIO_PHONE

to_phone = '+15558675309'

client = TwilioRestClient(TWILIO_ACCOUNT, TWILIO_TOKEN)

message = client.messages.create(to=to_phone, from_=TWILIO_PHONE, body="Message from VS")

print(message.sid)
