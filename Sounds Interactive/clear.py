from dotstar import Adafruit_DotStar
from gpiozero import LED

strip = Adafruit_DotStar(145)
n = 0

led_yellow = LED(12)
led_blue = LED(25)
led_green = LED(27)
strip.begin()

while n < 45:
    strip.setPixelColor(n, 0)
    strip.show()
    n += 1

led_yellow.off()
led_blue.off()
led_green.off()
strip.clear()
