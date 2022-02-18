# send SenseHat sensor data to Firebase database, and then read and print
# the 3 latest sensor data points from one teammates' Firebase database

import pyrebase
import random
import time
from sense_hat import SenseHat

# Create new Firebase config and database object
configKenny = {
  "apiKey": "KeyAIzaSyBEiVBDSoy1Tngr7fgg7KeWc6B--uj1niM",
  "authDomain": "sysc3010-lab3-9afcc.firebaseapp.com",
  "databaseURL": "https://sysc3010-lab3-9afcc-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010-lab3-9afcc.appspot.com"
}

# Create new Firebase config and database object
configCristian = {
  "apiKey": "AIzaSyDBjWGqOyGJKUKiFJytMG2WWlgAHBNCNek",
  "authDomain": "sysc3010-lab3-187fc.firebaseapp.com",
  "databaseURL": "https://sysc3010-lab3-187fc-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010-lab3-187fc.appspot.com"
}

firebaseKenny = pyrebase.initialize_app(configKenny)
dbKenny = firebaseKenny.database()

firebaseCristian = pyrebase.initialize_app(configCristian)
dbCristian = firebaseCristian.database()

# Write random numbers to database
def writeData():
    key = 0
    
    # initialize sensehat
    sense = SenseHat()
    sense.clear()

    while True:
      
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        
        # Each 'child' is a JSON key:value pair
        # temperature
        dbKenny.child("temperature").child(key).set(temperature)
        # humidity
        dbKenny.child("humidity").child(key).set(humidity)
        # pressure
        dbKenny.child("pressure").child(key).set(pressure)

        key = key + 1
        time.sleep(1)
        
        
def readData():
  # Returns the entry as an ordered dictionary (parsed from json)
  mySensorData = dbCristian.child("temperature").get()

  print("Parent Key: {}".format(mySensorData.key()))
  print("Parent Value: {}\n".format(mySensorData.val()))

  # Returns the dictionary as a list
  mySensorData_list = mySensorData.each()
  # Takes the last element of the list
  lastDataPoint = mySensorData_list[-1]

  print("Child Key: {}".format(lastDataPoint.key()))
  print("Child Value: {}\n".format(lastDataPoint.val()))
  
  # Returns the entry as an ordered dictionary (parsed from json)
  mySensorData = dbCristian.child("humidity").get()

  print("Parent Key: {}".format(mySensorData.key()))
  print("Parent Value: {}\n".format(mySensorData.val()))

  # Returns the dictionary as a list
  mySensorData_list = mySensorData.each()
  # Takes the last element of the list
  lastDataPoint = mySensorData_list[-1]

  print("Child Key: {}".format(lastDataPoint.key()))
  print("Child Value: {}\n".format(lastDataPoint.val()))
  
  # Returns the entry as an ordered dictionary (parsed from json)
  mySensorData = dbCristian.child("pressure").get()

  print("Parent Key: {}".format(mySensorData.key()))
  print("Parent Value: {}\n".format(mySensorData.val()))

  # Returns the dictionary as a list
  mySensorData_list = mySensorData.each()
  # Takes the last element of the list
  lastDataPoint = mySensorData_list[-1]

  print("Child Key: {}".format(lastDataPoint.key()))
  print("Child Value: {}\n".format(lastDataPoint.val()))


def main():
    #writeData() # uncomment to write data, keeping this line commented to print teammate data
    readData()
    
if __name__ == "__main__":  
    main() 