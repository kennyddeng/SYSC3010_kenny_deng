# displays  your  first  and  last  name continuously  on  your  SenseHAT  LED  display
from sense_hat import SenseHat

sense = SenseHat()

while True:
    sense.show_message("Kenny Deng")