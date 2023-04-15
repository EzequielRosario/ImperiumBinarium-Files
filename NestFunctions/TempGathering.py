from datetime import datetime
import json
import os
import TempSensor
import time

time.sleep(2)

def json_exists(fileName): #Check if file exists
    return os.path.exists(fileName)

def get_temp_filename(): #Sends name and directory of file
    dateNow = datetime.now()
    nowDay = now.date()
    nameFile = "/home/imperium/OutTemp/{}.json".format(nowDay)
    return (nameFile)

def get_temp_var(nestID): #Updates json file with new data
    #Information for current date and file
    now = datetime.now()
    curDay = now.date()
    curHour = now.hour 
    curMinute = now.minute
    curTime = '{:d}:{:02d}'.format(curHour, curMinute)
    localFolder = "/home/imperium/OutTemp/{}.json".format(curDay)

    #Obtain and set enviromental data on json
    dataList = TempSensor.enviromental_data() 
    hourInfo = {"hour":curTime,"temperature":dataList[1],"humidity":dataList[2]}
    
    if not json_exists(localFolder): #Create if file if not made yet
        variables = {"dailyReport":{"id":nestID,"date":curDay,"reports":[]}}
        varNew = json.dumps(variables, indent=1, sort_keys=True, default=str)
        with open(localFolder, 'w') as newFile:
            newFile.write(varNew)
            
    with open(localFolder, 'r+') as dailyFile: #Open and update information on json file
        time.sleep(1)
	tempFile = json.load(dailyFile)
	time.sleep(1)
        tempFile["dailyReport"]["reports"].append(hourInfo)
	time.sleep(1)
        dailyFile.seek(0)
	time.sleep(1)
        json.dump(tempFile,dailyFile,indent=1)

    #Save and return updated json file
    readyFile = open(localFolder, 'r')
    content = readyFile.read()
    return content
