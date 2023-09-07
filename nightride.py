# Libraries
import serial
from time import sleep
from gpiozero import LED, Button, MCP3008
import RPi.GPIO as GPIO
from pprint import pprint
import time

from lightModes import high, low, turnoff
# Set 


# Select GPIO Mode
GPIO.setmode(GPIO.BCM) 

# GPIO pin numbers
redPin = 12 
greenPin = 19 
bluePin = 13 
trig = 5      
echo = 26 
photocell = 6 
onIndicator = LED(17)
headlightToggleBtn = Button(18)

# Set headlight sate
headlight = 1

# Set pins as outputs or inputs 
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(photocell,GPIO.OUT)
GPIO.output(photocell,False)


def turnOff():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
    
def high():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)


def low():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.HIGH)
    GPIO.output(bluePin, GPIO.HIGH)
    


def distance():
    print("Distance Measurement In Progress")
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.output(trig, False)
    pulse_start = pulse_end = time.time()
    
    sleep(1)
    
    GPIO.output(trig, True)
    sleep(0.00001)
    GPIO.output(trig, False)
    
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
        
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    
    return round(pulse_duration * 17150, 2)

def intensity():
    GPIO.output(photocell,False)
    adc = MCP3008(channel=0)
    voltage = 5 * adc.value
    return voltage


def buttonPress():
    toggleHeadlight(headlight)


def senseLight():
    GPIO.output(photocell,False)
    
    if GPIO.output(photocell) == 0:
        state = 0
        
    while GPIO.output(photocell) == 1:
        state = 1
        
    return state


def toggleHeadlight(state):
    global headlight
    if state == 0 :
        headlight = 1
        high()
        print("Headlight is ON")
    else: 
        headlight = 0
        turnOff()
        print("Headlight is off")
        
    return headlight


try:
    # Turn off headlight 
    toggleHeadlight(headlight)
    
    # Delay program dtart for two seconds
    print("Waiting for progam to start")
    sleep(2)
    print("Progam started")
    
    while True:
        print("Programme Running", '*'*20)
        onIndicator.on()
        
        dist = distance()
        print ("Measured Distance = ", dist,'cm')
        
        # Read Light intensity from arduino
        ser = serial.Serial("/dev/ttyACM0",9600)
        ser.baudrate=9600
            
        read_ser = ser.readline().decode('utf-8').rstrip()
        
        if read_ser == 0 or read_ser == "" :
            print ("Measured Light Intensity =", read_ser, 'ce', "Light detected")
        else:
            print ("Measured Light Intensity =", read_ser, 'ce')
            
        if (((dist * 1) <= 15.00) and (headlight == 1)) and (read_ser == 0 or read_ser == ""):
            low()
            sleep(2)
        elif (((dist * 1) > 15.00) and (headlight == 1)) and (read_ser == 0 or read_ser == ""):
            high()
            
        headlightToggleBtn.when_pressed = buttonPress
            
        
except Exception as ex:
    pprint(ex)