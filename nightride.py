# Libraries
from time import sleep
from gpiozero import LED, Button
import RPi.GPIO as GPIO
from pprint import pprint
import time

from lightModes import Modes
from sensorReadings import Readings

# Instatiate the light modes class
readings = Readings(5, 26, 6)

# GPIO components
onIndicator = LED(17)
headlightToggleBtn = Button(18)


try:
    # Turn off headlight 
    readings.toggleHeadlight(readings.headlight)
    
    # Delay program dtart for two seconds
    print("Waiting for progam to start")
    sleep(2)
    print()
    while True:
        print("Programme Running", '*'*20)
        onIndicator.on()
        
        dist = readings.distance()
        
        read_ser = readings.lightIntensity()
        
        headlightToggleBtn.when_pressed = readings.buttonPress
            
        if (((dist * 1) <= 15.00) and (readings.headlight == 1)) and (read_ser == 0 or read_ser == ""):
            readings.lights.low()
            sleep(2)
        elif (((dist * 1) > 15.00) and (readings.headlight == 1)) and (read_ser == 0 or read_ser == ""):
            readings.lights.high()
        print(readings.headlight)
        
except Exception as ex:
    pprint(ex)