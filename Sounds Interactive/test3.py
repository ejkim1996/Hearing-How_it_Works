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

status = "main"

head  = 0               # Index of first 'on' pixel
tail  = -10             # Index of last 'off' pixel
color = 0xFF0000
color2 = color >> 8
color3 = color2 >> 8

def toggle_yellow(head, color, num_pixels_yellow, strip):
    led_yellow.on()
    strip.setPixelColor(head, color) # Turn on 'head' pixel
    strip.show()
    time.sleep(1.0 / 30)
    
    if blue.is_pressed == True:
        strip.clear()
        led_yellow.off()
        head = 0
        return "main"
    else:
        return "yellow"

def toggle_blue(head, color2, num_pixels_blue, strip):
    led_blue.on()
    strip.setPixelColor(head, color2)
    strip.show()
    time.sleep(1.0 / 30)

    if yellow.is_pressed == True:
        strip.clear()
        led_blue.off()
        head = 0
        return "main"
    else:
        return "blue"

while True:
    if status == "main":
        print("main")
        head = 0
        if yellow.is_pressed == True:
            status = "yellow"
        if blue.is_pressed == True:
            status = "blue"
        
    if status == "yellow":
        print("yellow")
        status = toggle_yellow(head, color, num_pixels_yellow, strip)
        head += 1
        if head > num_pixels_yellow:
            head = 0
            strip.clear()

    if status == "blue":
        print("blue")
        status = toggle_blue(head, color2, num_pixels_blue, strip)
        head += 1
        if head > num_pixels_blue:
            head = 0
            strip.clear()
