import requests
from sense_hat import SenseHat

# using Christian's API Keys
readKey = "EGIXYA7ZDC4DOSTZ"  
channelNumber = "1642554"
url = "https://api.thingspeak.com/channels/" + channelNumber + "/feeds.json"
results = 2
    
def main():
    # initialize sensehat
    sense = SenseHat()
    sense.clear()
   
    # payload includes the headers to be sent with the GET request
    # read the documentation for more information (https://docs.python-requests.org)
    payload = {'api_key': readKey, 'results': results}

    # Sends an HTTP GET request
    response = requests.get(url, params=payload)
    response = response.json()

    print("Channel Name: {}".format(response['channel']['name']))
    
    entries = response['feeds']

    # Print out the temperature at each entry's time
    for e in entries:
        print("At {}, the temperature was {}".format(e['created_at'], e['field1']))
        print("At {}, the humidity was {}".format(e['created_at'], e['field2']))
        print("At {}, the pressure was {}".format(e['created_at'], e['field3']))
        
        # output read entries from teammate (Christian) to SenseHat 
        sense.show_message("At {}, the temperature was {}".format(e['created_at'], e['field1']))
        sense.show_message("At {}, the humidity was {}".format(e['created_at'], e['field2']))
        sense.show_message("At {}, the pressure was {}".format(e['created_at'], e['field3']))
    
 
if __name__ == "__main__":  
    main() 

