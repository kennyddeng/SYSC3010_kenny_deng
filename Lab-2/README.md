Deliverables:\
Exercise 1: Complete. A screenshot of the of the sqlitebrowser/manager displaying the database you created (lab2-database-manager.png)\
Exercise 3: Complete. lab2-database-data-logger.py script and screenshot of database values\
Exercise 4: Incomplete. lab2-database-data-visualizer.py script and screenshot (lab2-database-plot.png)\
Section 3: Incomplete. Python  script  creating  and  modifying  a  database  based  on  web-scraped  information (lab2-database-JSON.py)

Exercise 3: To create sensorDB.db\
open terminal, navigate to working directory\
sqlite3 sensorDB.db
sqlite> BEGIN;
sqlite> CREATE TABLE sensordata (ID INTEGER, datetime TEXT, temperature NUMERIC, humidity NUMERIC, pressure NUMERIC);
sqlite> COMMIT;
