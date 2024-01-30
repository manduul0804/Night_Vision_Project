from gpiozero import LEDBoard, Button
from signal import pause
from time import sleep

button = Button(21)
leds = LEDBoard(25,24, pwm=False)


while True:
    button.when_pressed = leds.on
    button.when_pressed= leds.off

    