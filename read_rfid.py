#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    id, data = reader.read()
    print('Tag id: ', id)
    print('Data: ', data)
finally:
    GPIO.cleanup()
