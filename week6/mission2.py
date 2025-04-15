from gpiozero import LED, Button
from signal import pause

led = LED(20)
button = Button(25, pull_up=True, bounce_time=0.1)

button.when_pressed = led.toggle


pause()