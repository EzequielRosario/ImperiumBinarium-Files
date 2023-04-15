import requests
import os
from datetime import datetime
import nestConfig

#Set local repository to save data reports
localRepo = '/home/imperium/OutTemp/'

#AWS Constant
url = nestConfig.get_URL()

def sendIt():
    #Obtain current date
    now = datetime.now()
    curDay = '{}.json'.format(now.date()) 

    query = '''
    mutation PostDailyReport($dailyReport: PostDailyReportInput!) {
      postDailyReport(dailyReport: $dailyReport) {
        code
        message
      }
    }
    '''

    for fileNameToUpload in os.listdir(localRepo): #Go through every file in folder to send to cloud storage whenever available
        #Prepare file and send request
        readyFile = open(localRepo + fileNameToUpload, 'r')
        content = readyFile.read()
        try:
            res = requests.post(url, json={'query': query, 'variables': content})
        except Exception as error:
            return None
        print(res.status_code)
        if res.status_code == 200:
            if fileNameToUpload != curDay: #Delete the file if it's not from the current day
                os.remove(localRepo + fileNameToUpload)
        else:
            print(res.text)
            raise Exception("Query failed to run by returning code of {}.".format(res.text))
    return None
