from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.out,initial=GPIO.LOW)

while True:
    GPIO.output(32,GPIO.HIGH)
    sleep(2)
    GPIO.output(32,GPIO.HIGH)