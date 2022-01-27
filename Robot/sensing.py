#libraries
import RPi.GPIO as GPIO
import time


def get_distance():
    try:
        # GPIO setup
        GPIO.setmode(GPIO.BCM)

        #set pins
        GPIO_TRIG = 5
        GPIO_ECHO = 6

        GPIO.setup(GPIO_TRIG, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
        
        # activate Trigger
        GPIO.output(GPIO_TRIG, True)
        
        # end pulse after 0.01ms
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIG, False)
        
        # save ToD
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
        
        # save ToA
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
        
        # calculate time difference
        TimeElapsed = StopTime-StartTime
        # use half of speed of sonic to calculate distance
        distance = TimeElapsed * 17150
        
        print ("Distance Measured = %.1f cm" %distance)
        
        
    finally:
        GPIO.cleanup()
        return distance
    