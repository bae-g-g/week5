from gpiozero import LED, Button
from signal import pause

led = LED(20)
button = Button(25, pull_up=True)

led.source = button



pause()