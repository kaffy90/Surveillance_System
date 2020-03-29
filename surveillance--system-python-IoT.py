from gpiozero import Button
import RPi.GPIO as GPIO
from picamera import PiCamera
import time


button = Button(2)
pir = 4
camera = PiCamera()

GPIO.setwarnings(False)
GPIO.setup(pir, GPIO.IN)
print ('Sensor initializing........')
time.sleep(2)
print ('Sensor active :)')
camera.rotation = 180
camera.start_preview()

j = 0

def stop_camera():
    camera.stop_preview()
    exit()
    GPIO.cleanup()

def take_photo():
    while True:
        i = GPIO.input(pir)
        if i == 0:
            print ('No motion detected')
            time.sleep(3)
        elif i == 1:
            print ('Motion detected')
            global j
            j+= 1
            camera.capture('/home/pi/Surveillance/image_{0}s.jpg'.format(j))
            print ('a photo has been taken')
            time.sleep(3)

button.when_pressed = stop_camera

try:
    take_photo()
except KeyboardInterrupt:
    exit()


