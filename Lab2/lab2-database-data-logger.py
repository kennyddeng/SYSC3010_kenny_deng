#!/usr/bin/env python3
import sqlite3
from sense_hat import SenseHat
from time import sleep

# clear initial sensehat state
sense = SenseHat()
sense.clear()

# intial data
ID = 0;
datetime = 'datetime';

# connect to database file
dbconnect = sqlite3.connect("sensorDB.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

for i in range(10):
    temperature = sense.get_temperature();
    humidity = sense.get_humidity();
    pressure = sense.get_pressure();
    #execute insert statement
    cursor.execute('''INSERT INTO sensordata values (?, datetime('now'), ?, ?, ?)''',
                   (ID, temperature, humidity, pressure));
    ID += 1;
    sleep(1);
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM sensordata');
#print data
for row in cursor:
    print(row['ID'],row['datetime'], row['temperature'],
          row['humidity'], row['pressure']);
#close the connection
dbconnect.close();
