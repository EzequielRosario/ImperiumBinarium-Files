import requests
import os
import json
import nestConfig

#AWS Constants
target_url = nestConfig.get_URL()

#Set Variables
def sendPic(nestID):
    monitorId = nestID
    localFileDirectory = '/home/imperium/OutCam/' #Set camera output directory
    
    # Presigned URL Query
    query = '''
        query GetPresignedURL($filename: String!, $id: String!) {
          getPresignedURL(filename: $filename, id: $id) {
            url
            fields
          }
        }
        '''
    
    for fileNameToUpload in os.listdir(localFileDirectory): #Go through every file in folder to send to cloud storage whenever available
        content = json.dumps({'id': monitorId, 'filename': fileNameToUpload}) #Assign nest name to be checked

        # Query Result
        request = requests.post(target_url, json={'query': query, 'variables': content})
        res = request.json()

        # Get URL and Fields from Query
        url = res['data']['getPresignedURL']['url']
        fields = json.loads(res['data']['getPresignedURL']['fields'])

        # Prepare file
        files = {'file': open(localFileDirectory + fileNameToUpload, 'rb')}

        #Upload File
        r = requests.post(url, fields, files=files)
        print(r.status_code)
        if r.status_code == 204: #Delete picture when sent successfully to cloud storage
            os.remove('{}{}'.format(localFileDirectory, fileNameToUpload))
        #print(r.headers)
    return None
sendPic('Pitaya1')
