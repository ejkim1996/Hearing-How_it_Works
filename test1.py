from gpiozero import Button
from dotstar import Adafruit_DotStar
import time

numpixels = 30

strip = Adafruit_DotStar(numpixels)

strip.begin()
strip.setBrightness(64)

button = Button(22)

head  = 0               # Index of first 'on' pixel
tail  = -10             # Index of last 'off' pixel
color = 0xFF0000

while True:
    button.wait_for_press()
    strip.setPixelColor(head, color) # Turn on 'head' pixel
    #strip.setPixelColor(tail, 0)     # Turn off 'tail'
    strip.show()
    time.sleep(1.0 / 30)             # Pause 20 milliseconds (~50 fps)

    head += 1                        # Advance head position
    if(head >= numpixels):           # Off end of strip?
	    head    = 0              # Reset to start
	    color >>= 8              # Red->green->blue->black
	    if(color == 0): color = 0xFF0000 # If black, reset to red

    #tail += 1                        # Advance tail position
    #if(tail >= numpixels): tail = 0  # Off end? Reset
