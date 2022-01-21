from sense_hat import SenseHat
from time import sleep
#!/usr/bin/env python3
import sqlite3





#connect to database file
dbconnect = sqlite3.connect("sensorDB.db");

#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

sense = SenseHat();
sense.clear();

id = 0;
date = 'now';
time = 'now';
#temperature = 0;
#humidity = 0;
#pressure = 0;
# temperature
temperature = float(sense.get_temperature());
# humidity
humidity = sense.get_humidity();
# pressure
pressure = sense.get_pressure();

for i in range(10):
	cursor.execute('''insert into sensordata values ('id', DATE('now'), TIME('now'), 'temperature', 0, 0)''');
	#cursor.execute('''insert into sensordata values (?,?,?,?,?,?)''',('id', date, ('now'), 'temperature', 0, 0));
	id += 1;
dbconnect.commit();
cursor.execute('SELECT * FROM sensordata');

for row in cursor:
	print(row['id'], row['tdate'], row['ttime'], row ['temperature'], row ['humidity'], row ['pressure'] );
	
dbconnect.close(); 

#BEGIN;

#for i in range(10):
	#execute insert statement
	# CREATE TABLE sensordata(id INTEGER, tdate DATE, ttime TIME, temperature NUMERIC, humidity NUMERIC, pressure NUMERIC);
	#INSERT INTO sensordata values(integer(id), date('now'), time('now'), numeric(sense.get_temperature()), numeric(sense.get_humidity()), numeric(sense.get_pressure()));
    #cursor.execute(, (id, date('now'), time('now'), numeric(sense.get_temperature()), numeric(sense.get_humidity()), numeric(sense.get_pressure())) );
    #id += 1;
#dbconnect.commit();
    # temperature
#temperature = sense.get_temperature();
	# humidity
#humidity = sense.get_humidity();
	# pressure
#pressure = sense.get_pressure();









