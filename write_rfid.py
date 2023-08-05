#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('Input data to write: ')
    print('Tap to write data')
    reader.write(text)
    print('Updated')
finally:
    GPIO.cleanup()
