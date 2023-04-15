import os
import time
time.sleep(5) #Await system to boot up or restart
os.system("timedatectl") #Synchronize clock with internet timezone if available
import schedule
import nestConfig
import Motion
import TempGathering
import TempSensor
import HourlyCheckIn
import TempDailyReport
from threading import Thread
from functools import partial

nestID = nestConfig.get_ID() #Obtain nest name
TempSensor.enviromental_data() #Initialize sensor to give correct values
hourCheck = nestConfig.get_hourCheck() #Scheduled time for hourly temperature readings and internet connectivity.

HourlyCheckIn.checkIn(nestID) #Check connection with internet when booting up or when Main.py restarts.

def _sendDailyReport(): #Send enviromental data to backend
    TempDailyReport.sendIt()
    
def _runTempScript(): #Obtain and send enviromental data and check connection to backend
    time.sleep(1)
    HourlyCheckIn.checkIn(nestID)
    TempGathering.get_temp_var(nestID)
    print("got enviromental data")
    _sendDailyReport()
    
def _takePic(): #Takes and sends pictures to backend when motion is detected 
    Motion.detect(nestID)

def _wifiScript(): #Checks internet connection and attempts to reconnect if not connected.
    while True:
        os.system("sudo /home/imperium/reconnect-wifi.sh")
        return None

def _schedule(): #Run necesssary functions at specific time intervals
    schedule.every(hourCheck).minutes.do(_runTempScript)
    schedule.every(5).minutes.do(_wifiScript)
    while True:
        schedule.run_pending() #Keeps the scheduler running at all times
        time.sleep(1)

if __name__ == "__main__":
    while True: 
        try: #Run schedule at the same time with camera
            Thread(target=partial(_schedule)).start()
            _takePic() 
        except: #Re-run script if error occurs
            os.system("sudo python3 /home/imperium/Desktop/NestFunctions/Main.py") 
else:
    os.system("sudo python3 /home/imperium/Desktop/NestFunctions/Main.py")
