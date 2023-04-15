import time
import board
import Adafruit_DHT

dhtDevice = Adafruit_DHT.DHT22  #Initialize temperature/humidity sensor
pin = 17

def _take_dht_data(): #Assign enviromental data to list
    sensor_data = []
    try:
        humidity, temperature = Adafruit_DHT.read_retry(dhtDevice, pin)
        sensor_data.insert(0,round(temperature,2)) #celsius
        fahrenheit = sensor_data[0] * (9 / 5) + 32
        sensor_data.insert(1,round(fahrenheit,2)) #fahrenheit
        sensor_data.insert(2,round(humidity,1)) #humidity
    
    except RuntimeError as error:        
        return None
        
    except TypeError as error:
        return None
    
    except Exception as error:
       # dhtDevice.exit()
        raise error
    print(sensor_data)
    return sensor_data

def enviromental_data(): #Call to obtain enviromental data
    my_data = _take_dht_data()
    while(my_data == None): #Retry until successful measurement is done
        time.sleep(3.0)
        my_data = _take_dht_data()
    else:
        return my_data
