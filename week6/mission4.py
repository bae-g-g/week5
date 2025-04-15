from gpiozero import LED, Button,LEDBoard
from signal import pause

leds = LEDBoard(24,23,21,20)
button = Button(25, pull_up=True, bounce_time=0.1)
count = 0

def countup():
    global count
    count = (count+1)%16
    leds.value = (1&count,  2&count,  4&count,  8&count)


button.when_pressed = countup

pause()