from gpiozero import LED, Button
from signal import pause
import photobooth

# Define the GPIO pin number you want to use
gpioLed = 4
gpioButton = 14

# Create an LED object for the specified GPIO pin
led = LED(gpioLed)
button = Button(gpioButton)

led.on()
button.when_pressed = onPress

def onPress():
    led.off()
    photobooth.takePhoto()
    led.on()

pause()
