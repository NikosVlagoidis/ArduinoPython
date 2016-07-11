import serial
import thingspeak
import time
import requests
import json
import urllib


ch = thingspeak.Channel(132764)
arduino = serial.Serial('COM4', 9600, timeout=.1)
while True:

        data = arduino.readline()[:-3]  # the last bit gets rid of the new-line chars
        if data:
            forupload = (str(data)[2:-1])
            print(forupload)
            url = 'https://api.thingspeak.com/update?key=ATVCL0CLGW39ZY8N&field1='+forupload
            filehandle  = requests.get(url)
        time.sleep(16)
