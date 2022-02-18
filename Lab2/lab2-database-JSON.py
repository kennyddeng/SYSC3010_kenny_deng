from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"  # If it doesn’t work, get your own. 
# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

current = data["main"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
print ("Humidity: %d%%" % current["humidity"])
print ("Pressure: %d" % current["pressure"] )

current = data["wind"]
print ("Wind : %d" % current["speed"])

# connect to database file
dbconnect = sqlite3.connect("jsonDB.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

#execute insert statement
cursor.execute('''INSERT INTO jsondata values (?, ?)''', (city, current["speed"]));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM jsondata');
#print data
for row in cursor:
    print(row['city'],row['wind']);
#close the connection
dbconnect.close();
