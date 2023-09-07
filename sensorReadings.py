import RPi.GPIO as GPIO
import time
import serial
from lightModes import Modes

class Readings():
    def __init__(self, trig, echo, photocell):
        self.trig = trig
        self.echo = echo 
        self.photocell = photocell
    
        # Set headlight sate
        self.headlight = 1 # to indicate the on state

        #Select GPIO Mode
        GPIO.setmode(GPIO.BCM)
        
        #disable warnings (optional)
        GPIO.setwarnings(False)  
        
        # Set pins as outputs or inputs 
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        GPIO.setup(photocell, GPIO.OUT)
        GPIO.output(photocell, False)
        
        self.lights = Modes(12, 19, 13)

    def distance(self):
        print("Distance Measurement In Progress")
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, False)
        pulse_start = pulse_end = time.time()
        
        time.sleep(1)
        
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
            
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        
        dist = round(pulse_duration * 17150, 2)
        print ("Measured Distance = ", dist, 'cm')
        
        return dist
    

    def buttonPress(self):
        self.toggleHeadlight(self.headlight)


    def toggleHeadlight(self, state):
        if state == 0 :
            self.headlight = 1
            self.lights.high()
            print("Headlight is ON")
        else: 
            self.headlight = 0
            self.lights.turnOff()
            print("Headlight is OFF")
            
        return self.headlight


    def lightIntensity(self):
        print("Measuring Light Intensity")
        
        # Read Light intensity from arduino
        ser = serial.Serial("/dev/ttyACM0",9600)
        ser.baudrate=9600
            
        read_ser = ser.readline().rstrip()
        
        if read_ser == 0 or read_ser == "" :
            print ("Measured Light Intensity =", read_ser, 'ce', "Light detected")
        else:
            print ("Measured Light Intensity =", read_ser, 'ce')
            
        return read_ser