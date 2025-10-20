from time import sleep
from picamera import PiCamera
print(camera)
camera=PiCamera()
camera.resolution(1024,768)
camera.start_preview()
sleep(5)
camera.capture("home/pi/Desktop/test1.py")
camera.stop_preview(5 )