import RPi.GPIO as GPIO 
import time 
import Cam
import CamUpload
import nestConfig

GPIO.setmode(GPIO.BCM) #Set GPIO pin numbering
pir = 4 #Associate pin 4 to pir

def _PICTURE(theId): #Calls the camera to take a picture
    Cam.TAKEPIC(theId)

def detect(Id):
    GPIO.setup(pir, GPIO.IN) #Set pin as GPIO in
    time.sleep(5) #Waiting 5 seconds for the sensor to initiate
    while True:
        if GPIO.input(pir): #When pin gives a HIGH, it means motion has been detected
            time.sleep(0.9) #Delay check to avoid false positives
            if GPIO.input(pir):
                print("Motion detected")
                _PICTURE(Id)
                CamUpload.sendPic(Id)
                time.sleep(10) #Delay to avoid multiple detection
        else:
            time.sleep(0.5) #Scan for movement every half a second
