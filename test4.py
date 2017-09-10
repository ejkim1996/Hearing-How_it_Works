from gpiozero import Button
from gpiozero import LED
from dotstar import Adafruit_DotStar
from signal import pause
from pygame import mixer
import time

num_pixels_yellow = 30
num_pixels_blue = 45

led_yellow = LED(12)
led_blue = LED(25)

button_yellow = Button(22)
button_blue = Button(24)

strip = Adafruit_DotStar(60)
strip.begin()
strip.setBrightness(64)
speed = 30              #bigger values make it faster

status = "main"

head  = 0               # Index of first 'on' pixel
color = 0xFF0000
color2 = color >> 8
color3 = color2 >> 8

mixer.init()
sound1 = mixer.Sound("sample1.wav")
sound2 = mixer.Sound("sample2.wav")


def toggle_yellow(head, color, num_pixels_yellow, strip):
    led_yellow.on()
    strip.setPixelColor(head, color) # Turn on 'head' pixel
    strip.show()
    time.sleep(1.0 / speed)
    
    if button_blue.is_pressed == True:
        strip.clear()
        led_yellow.off()
        sound1.stop()
        return "main"
    elif mixer.get_busy() == False:
        turn_off_lights(num_pixels_yellow)
        led_yellow.off()
        return "main"
    else:
        return "yellow"

def toggle_blue(head, color2, num_pixels_blue, strip):
    led_blue.on()
    strip.setPixelColor(head, color2)
    strip.show()
    time.sleep(1.0 / speed)

    if button_yellow.is_pressed == True:
        strip.clear()
        led_blue.off()
        sound2.stop()
        return "main"
    elif mixer.get_busy() == False:
        turn_off_lights(num_pixels_blue)
        led_blue.off()
        return "main"
    else:
        return "blue"

def turn_off_lights(num_pixels):
    n = 0
    while n < num_pixels:
        strip.setPixelColor(n, 0)
        strip.show()
        n += 1

while True:
    if status == "main":
        print("main")
        head = 0
        if button_yellow.is_pressed == True:
            sound1.play()
            status = "yellow"
        if button_blue.is_pressed == True:
            sound2.play()
            status = "blue"
        
    elif status == "yellow":
        print("yellow")
        status = toggle_yellow(head, color, num_pixels_yellow, strip)
        head += 1
        if head > num_pixels_yellow:
            head = 0
            strip.clear()
        

    elif status == "blue":
        print("blue")
        status = toggle_blue(head, color2, num_pixels_blue, strip)
        head += 1
        if head > num_pixels_blue:
            head = 0
            strip.clear()
