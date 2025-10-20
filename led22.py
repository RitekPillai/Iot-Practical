from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(7,GPIO.OUT,initial=GPIO.HIGH)

while True:
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(7,GPIO.LOW)
    sleep(5)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(7,GPIO.HIGH)
    sleep(5)