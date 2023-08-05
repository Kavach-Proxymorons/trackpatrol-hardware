#!/usr/bin/env python

import sys
import time
import datetime
import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

url = 'https://trackpatrol.onrender.com/api/v1/hardware/pushData/?useMap=true'
reader = SimpleMFRC522()

try:
    while True:
        id, _ = reader.read()
        print('scanned: ', id)
        r = requests.post(url, json={
            'hardware_id': sys.argv[1],
            'secret': sys.argv[2],
            'timestamp': datetime.datetime.now(tz=datetime.timezone.utc).isoformat(),
            'data': id
        })
        if r.json()['status'] == 200:
            print('marked: ', id)
        else:
            print('failed: ', id)
        time.sleep(1)
finally:
    GPIO.cleanup()
