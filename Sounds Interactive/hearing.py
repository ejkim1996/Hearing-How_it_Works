from gpiozero import Button
from gpiozero import LED
from dotstar import Adafruit_DotStar
from signal import pause
from pygame import mixer
import time

#Dotstar Visual Settings
lighting_type = "strand"
brightness = 64
speed = 50                                      #bigger values make it faster

#mixer setup for audio
mixer.init()
sound_low_pitch = mixer.Sound("FrenchHorn.wav")
sound_medium_pitch = mixer.Sound("Sax.wav")
sound_high_pitch = mixer.Sound("Flute.wav")

#Variables for low pitch sound
num_pixels_low_pitch = 143                      #number of lights to turn on
led_low_pitch = LED(12)
button_low_pitch = Button(22)                   #yellow button currently
color_low_pitch = 0xFF0000                      #Red

#Variables for medium pitch sound
num_pixels_medium_pitch = 70
led_medium_pitch = LED(25)
button_medium_pitch = Button(24)                #blue button currently
color_medium_pitch = color_low_pitch >> 8       #Green

#Variables for medium pitch sound
num_pixels_high_pitch = 35
led_high_pitch = LED(27)
button_high_pitch = Button(23)                  #green button currently
color_high_pitch = color_medium_pitch >> 8      #Blue

#Dotstar setup and variables for LED strip
strip = Adafruit_DotStar(144)
strip.begin()
strip.setBrightness(brightness)
status = "main"
head  = 0                                       #Index of first 'on' pixel
tail = -10                                      #Index of last 'off' pixel

def light_strip(color, num_pixels, led, status, button1, button2, sound):
    global head, tail
    if lighting_type == "continuous":
        led.on()
        strip.setPixelColor(head, color)
        strip.show()
        time.sleep(1.0 / speed)
        head += 1
        if head > num_pixels:
            head = 0
            strip.clear()
            strip.setPixelColor(num_pixels, color)

    elif lighting_type == "strand":
        led.on()
        strip.setPixelColor(head, color)
        if (tail != num_pixels - 1):
            strip.setPixelColor(tail, 0)
        strip.show()
        time.sleep(1.0 / speed)
        head += 1
        tail += 1
        if head >= num_pixels: head = 0
        if tail >= num_pixels: tail = 0
   
    if (mixer.get_busy() == False):
        strip.clear()
        strip.show()
        led.off()
        return "main"

    return check_button_press(status, led, button1, button2, sound)

def check_button_press(status, led, button1, button2, sound):
    if (button1.is_pressed == True or button2.is_pressed == True):
        strip.clear()
        led.off()
        sound.stop()
        return "main"
    else:
        return status

while True:
    if status == "main":
        print("main")
        head = 0
        tail = -10

        if button_low_pitch.is_pressed == True:
            sound_low_pitch.play()
            status = "low pitch"

        if button_medium_pitch.is_pressed == True:
            sound_medium_pitch.play()
            status = "medium pitch"

        if button_high_pitch.is_pressed == True:
            sound_high_pitch.play()
            status = "high pitch"
        
    elif status == "low pitch":
        print("low pitch")
        status = light_strip(color_low_pitch, num_pixels_low_pitch, led_low_pitch, 
            status, button_medium_pitch, button_high_pitch, sound_low_pitch)

    elif status == "medium pitch":
        print("medium pitch")
        status = light_strip(color_medium_pitch, num_pixels_medium_pitch, led_medium_pitch, 
            status, button_low_pitch, button_high_pitch, sound_medium_pitch)

    elif status == "high pitch":
        print("high pitch")
        status = light_strip(color_high_pitch, num_pixels_high_pitch, led_high_pitch, 
            status, button_low_pitch, button_medium_pitch, sound_high_pitch)