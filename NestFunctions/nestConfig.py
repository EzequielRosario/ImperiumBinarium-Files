nestID = 'Pitaya1' #Replace this ID when installing a new system.

GraphQL_URL = 'https://7p3h5obsk6.execute-api.us-east-1.amazonaws.com/prod/' #Link to query that receives the temperature reports.

#Schedule values that specify when you wish for certain functions to happen.
hourCheckTime = 60 #Amount of minutes to wait and run scheduled program.
#If you wish to add more cycles, you can copy/paste more schedule functions in the _schedule() function.

def get_ID():
    return nestID

def get_URL():
    return GraphQL_URL

def get_hourCheck():
    return hourCheckTime

def get_tempReport():
    return tempReportTime


#VNC login for wireless connection to Raspberry Pi
#User: imperium
#Password: binarium
#Password Hash: $2y$10$WwmUGORPd6iMZUAd3EG/Qe7SngKZmN0f.QHcu3Ipk16rhOKkQYTHG
