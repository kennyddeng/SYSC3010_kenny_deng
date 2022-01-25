import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to database file
dbconnect = sqlite3.connect("sensorDB.db")

df = pd.read_sql_query("SELECT * FROM sensordata", dbconnect)


df.plot()
plt.show()
