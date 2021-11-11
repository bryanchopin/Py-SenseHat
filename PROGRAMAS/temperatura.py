# This file has been written to your home directory for convenience. It is
# saved as "/home/david/temperature-2021-10-20-17-54-53.py"

#from sense_emu import SenseHat
from sense_hat import SenseHat
import time

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.temp
    print('Temperatura: %.1fC' % temp)
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
    time.sleep(0.5)
