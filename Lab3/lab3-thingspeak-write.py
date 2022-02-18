from  sense_hat import SenseHat  
import requests
from time import sleep

sendKey = "H19EA20R6QORR1KS"  
url =  "https://api.thingspeak.com/update"
    
def main():
    # initialize sensehat
    sense = SenseHat()
    sense.clear()
    
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    
    while(True):
        # payload includes the headers to be sent with the GET request  
        # read the documentation for more information (https://docs.python-requests.org)  
        payload = {'field1' : temperature, 'field2' : humidity, 'field3' : pressure, 'api_key' : sendKey}
        
        try:  
            # Sends an HTTP GET request  
            response = requests.get(url, params=payload)  
            #  The library can also decode JSON responses 
            response = response.json()  
     
            print(response)  
        except:  
            print( "Connection Failed" )
        sleep(120)
 
if __name__ == "__main__":  
    main() 
