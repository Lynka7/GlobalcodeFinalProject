#LIBRARIES
from time import sleep
from gpiozero import LED
import RPi.GPIO as GPIO
from pprint import pprint


import time
#import board
#sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

led1 = LED(17)

#Select GPIO Mode
GPIO.setmode(GPIO.BCM) #  GPIO.setmode(GPIO.BOARD)

# GPIO pin numbers
redPin = 12 #17
greenPin = 19 #18
bluePin = 13 # 27
trig = 5 # 11       
echo = 26 # 13

#set pins as outputs
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def high():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)

def low():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.HIGH)
    GPIO.output(bluePin, GPIO.HIGH)
    
    
def ultraRead():
    #GPIO.output(trig, GPIO.HIGH)
    
    start = time.time ()
            
    if GPIO.input(echo) == 1:
        end = time.time()
        distance = ((end - start) * 34300) / 2
        
        print ("distance:", distance, "cm")
        print("echo -- ",GPIO.input(echo))
        #time.sleep(.1)
        

def distance():
    # set Trigger to HIGH
    GPIO.output(trig, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trig, False)
 
    StartTime = StopTime = time.time()
 
    # save StartTime
    if GPIO.input(echo) == 0:
        StartTime = time.time()
 
    # save stop time 
    if GPIO.input(echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance   


  
try:
    while True:
        print("programme running>>>")
        led1.on()
        #high()
        #sleep(1)
        #low()
        #sleep(1)
        dist = distance()
        print ("Measured Distance = ", dist,'cm')
        #sleep(1)
        #break
        
        
        #time.sleep (0.00001) # 10 microseconds
        #GPIO.output(trig, False)
        
except Exception as ex:
    pprint(ex)