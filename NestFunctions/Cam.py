from datetime import datetime
from picamera2 import Picamera2, Preview
import time

cam = Picamera2() #Initialize camera
camConfig = cam.create_still_configuration(main={"size":(640,480)}, lores={"size":(100,100)}, display="lores") #Set resolution "size". "lores" is for preview.
cam.configure(camConfig) #Set configuration on camera

def TAKEPIC(nestID):
    time.sleep(1)
    #Set information for picture file name to current name, followed by the nest name
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%SZ{}".format(nestID))
    camRepo = "/home/imperium/OutCam/{}.jpg".format(dt_string) #Set camera output repository
    
    #Take picture
    cam.start()
    cam.capture_file(camRepo)
    cam.stop_preview()
    cam.stop()
    print("Done") #Confirm picture taken
