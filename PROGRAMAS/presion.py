#from sense_emu import *
from sense_hat import *

Gn = (0, 255, 0)
hat = SenseHat()
while True:
    msg = 'Presion: %.1fmbar' % hat.pressure
    print(msg)
    hat.show_message(msg, 0.05, Gn)
