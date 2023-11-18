from gpiozero import LED, Button
from signal import pause
import photobooth

gpioLed = 4
gpioButton = 14
led = LED(gpioLed)
button = Button(gpioButton)

def onPress():
    led.off()
    photobooth.takePhoto()
    led.on()

led.on()
button.when_pressed = onPress
pause()
