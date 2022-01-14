# displays the temperature, pressure, and humidity on your SenseHAT LED display
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# print temperature on SENSEHAT LED display
temp = sense.get_temperature()
sense.show_message(str(temp))

# print pressure on SENSEHAT LED display
pressure = sense.get_pressure()
sense.show_message(str(pressure))

# print humidity on SENSEHAT LED display
humidity = sense.get_humidity()
sense.show_message(str(humidity))