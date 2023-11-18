from gpiozero import LED, Button
from signal import pause
import photobooth

gpioLed = 4
gpioButton = 14
led = LED(gpioLed)
button = Button(gpioButton)

def onPress():
    led.off()
    try:
        photobooth.takePhoto()
        led.on()
    except Exception as e:
        print(f"Error taking photo: {e}")
        led.blink(0.3, 0.3)

led.on()
button.when_pressed = onPress
pause()
