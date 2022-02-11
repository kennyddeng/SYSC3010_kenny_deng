from sense_hat import SenseHat
from time import sleep

# returns a SenseHat instance
def get_sensehat():
    return SenseHat()

# input SenseHat instance and flash_time
# SenseHat display flashes red (1 sec on, 1 sec off) for duration of flash_time
# At end of flash_time, SenseHat display should be off
def alarm(sense, flash_time):
    count = 0
    while count < flash_time:
        sense.clear(255, 0, 0)
        sleep(1)
        sense.clear()
        sleep(1)
        count += 2
        

