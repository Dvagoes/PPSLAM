import RPi.GPIO as GPIO
import time


#GPIO setup
GPIO.setmode(GPIO.BCM)

GPIO_RB = 4
GPIO_RF = 17
GPIO_LB = 27
GPIO_LF = 22

GPIO.setup(GPIO_LF, GPIO.OUT)
GPIO.setup(GPIO_LB, GPIO.OUT)
GPIO.setup(GPIO_RF, GPIO.OUT)
GPIO.setup(GPIO_RB, GPIO.OUT)

def turn_left(x):
    # set left backwards and right forwards
    # accept time of rotation as input
    GPIO.output(GPIO_LB, GPIO.HIGH)
    GPIO.output(GPIO_RF, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(GPIO_LB, GPIO.LOW)
    GPIO.output(GPIO_RF, GPIO.LOW)
    return

def turn_right(x):
    # set right backwards and left forwards
    # accept time of rotation as input
    GPIO.output(GPIO_LF, GPIO.HIGH)
    GPIO.output(GPIO_RB, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(GPIO_LF, GPIO.LOW)
    GPIO.output(GPIO_RB, GPIO.LOW)
    return

def move_forward(x):
    # set both forwards
    # accept x=time of movement as input
    GPIO.output(GPIO_LF, GPIO.HIGH)
    GPIO.output(GPIO_RF, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(GPIO_LF, GPIO.LOW)
    GPIO.output(GPIO_RF, GPIO.LOW)
    return

def move_backward(x):
    # set both backwards
    # accept time of movement as input
    GPIO.output(GPIO_LB, GPIO.HIGH)
    GPIO.output(GPIO_RB, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(GPIO_LB, GPIO.LOW)
    GPIO.output(GPIO_RB, GPIO.LOW)
    return

turn_left(2)
turn_right(2)
move_forward(2)
move_backward(2)
GPIO.cleanup()