from gpiozero import LED
from time import sleep

led = LED(25)
led1 = LED(17)
while True:
    led.on()
    led1.on()
    sleep(5)
    led.off()
    led1.off()
    sleep(10)
