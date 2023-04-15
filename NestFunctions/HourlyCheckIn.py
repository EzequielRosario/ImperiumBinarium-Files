import requests
import json
import nestConfig

#AWS Constants
url = nestConfig.get_URL() 
query = '''
mutation Mutation($id: String!) {
  checkIn(id: $id) {
    code
    message
  }
}
'''

def checkIn(nestID):
    #Ensure nest is connected to the backend
    content = json.dumps({'id':nestID}) #Assign nest name to be checked
    try:
        res = requests.post(url, json={'query': query, 'variables': content})
    except Exception as error:
        return None
    if res.status_code == 200:
        print(res.status_code)
    else:
        raise Exception("Query failed to run by returning code of {}.".format(res.text))
    return None
