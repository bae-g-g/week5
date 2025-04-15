from gpiozero import LED, Button,LEDBoard
from signal import pause

leds = LEDBoard(20,21,23,24)

button = Button(25, pull_up=True, bounce_time=0.1)
   
button.when_pressed = lambda:[led.blink(on_time=1, off_time=0,n=1,background=False) for led in leds]

pause()