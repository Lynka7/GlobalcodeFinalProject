import RPi.GPIO as GPIO

class Modes:
    def __init__(self,red,green,blue) :
        self.redPin = red 
        self.greenPin = green 
        self.bluePin = blue 
        
        #Select GPIO Mode
        GPIO.setmode(GPIO.BCM)
        
        #disable warnings (optional)
        GPIO.setwarnings(False)  

        #set pins as outputs
        GPIO.setup(self.redPin,GPIO.OUT)
        GPIO.setup(self.greenPin,GPIO.OUT)
        GPIO.setup(self.bluePin,GPIO.OUT)


    def turnOff(self):
        GPIO.output(self.redPin,GPIO.LOW)
        GPIO.output(self.greenPin,GPIO.LOW)
        GPIO.output(self.bluePin,GPIO.LOW)
        
        
    def high(self):
        GPIO.output(self.redPin,GPIO.LOW)
        GPIO.output(self.greenPin,GPIO.HIGH)
        GPIO.output(self.bluePin,GPIO.LOW)


    def low(self):
        GPIO.output(self.redPin, GPIO.LOW)
        GPIO.output(self.greenPin, GPIO.HIGH)
        GPIO.output(self.bluePin, GPIO.HIGH)
        
