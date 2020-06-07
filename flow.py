import RPi.GPIO as GPIO
import time, sys
import json 
file = open('flow.json', 'w')
pulse_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulse_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
def countPulse1(channel):
        count+=1
        print("Number of revolution of wheel of flow sensor:")
        print(count)
        pulsecount=(count/4.5)*60
        litresperhour=pulsecount
        file.write(litresperhour)
        file.close() 
GPIO.add_event_detect(pulse_pin, GPIO.RISING, callback=countPulse1)

try:
        while True:
                print("Inside while starting")
                time.sleep(10)
                print("Inside while ending")
                time.sleep(10)
except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()