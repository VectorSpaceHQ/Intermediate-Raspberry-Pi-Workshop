#!/bin/sh

apt-get update
apt-get install -y python3-gpiozero
apt-get install -y python3-w1thermsensor

python3 -m pip install twilio
python3 -m pip install phant

grep -q "^dtoverlay=w1-gpio" /boot/config.txt

if [ $? -ne 0 ]
  then echo "\ndtoverlay=w1-gpio\n" >> /boot/config.txt
fi

echo "\nPlease reboot to finish installation\n"
