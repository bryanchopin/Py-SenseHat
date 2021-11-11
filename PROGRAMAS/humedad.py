# This file has been written to your home directory for convenience. It is
# saved as "/home/david/humidity-2021-10-20-17-54-50.py"

#from sense_emu import SenseHat
from sense_hat import SenseHat
import time

sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)

while True:
    humidity = sense.humidity
    print('Humedad: %.1f%%' % humidity)
    humidity_value = 64 * humidity / 100
    pixels = [green if i < humidity_value else white for i in range(64)]
    sense.set_pixels(pixels)
    time.sleep(0.5)
