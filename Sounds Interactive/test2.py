from gpiozero import Button
from gpiozero import LED
from dotstar import Adafruit_DotStar
import time
from signal import pause

num_pixels_yellow = 30
num_pixels_blue = 45

strip = Adafruit_DotStar(60)

strip.begin()
strip.setBrightness(64)

led_yellow = LED(12)
led_blue = LED(25)

yellow = Button(22)
blue = Button(24)

head  = 0               # Index of first 'on' pixel
tail  = -10             # Index of last 'off' pixel
color = 0xFF0000
color2 = color >> 8
color3 = color2 >> 8

def toggle_yellow(head, color, num_pixels_yellow, strip):
    print("toggle")
    led_yellow.on()
    strip.setPixelColor(head, color) # Turn on 'head' pixel
    strip.show()
    time.sleep(1.0 / 30)             # Pause 20 milliseconds (~50 fps)
    head += 1                        # Advance head position
    if head > num_pixels_yellow:
        head = 0
        strip.clear()
    if blue.is_pressed == True:
        strip.clear()
        led_yellow.off()
        toggle_blue(0, color2, num_pixels_blue, strip)
    else:
        toggle_yellow(head, color, num_pixels_yellow, strip)

def toggle_blue(head, color2, num_pixels_blue, strip):
    print("blue")
    led_blue.on()
    strip.setPixelColor(head, color2)
    strip.show()
    time.sleep(1.0 / 30)
    head += 1
    if head > num_pixels_blue:
        head = 0
        strip.clear()

    if yellow.is_pressed == True:
        strip.clear()
        led_blue.off()
        toggle_yellow(0, color, num_pixels_yellow, strip)
    else:
        toggle_blue(head, color2, num_pixels_blue, strip)

while True:
    #yellow.wait_for_press()
    if yellow.is_pressed == True:
        print("y true")
        toggle_yellow(head, color, num_pixels_yellow, strip)
    #blue.wait_for_press()
    if blue.is_pressed == True:
        print("b true")
        toggle_blue(head, color2, num_pixels_blue, strip)
    
