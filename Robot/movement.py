import RPi.GPIO as GPIO
import time


# GPIO setup
class Move:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.GPIO_RB = 4
        self.GPIO_RF = 17
        self.GPIO_LB = 27
        self.GPIO_LF = 22

        GPIO.setup(self.GPIO_LF, GPIO.OUT)
        GPIO.setup(self.GPIO_LB, GPIO.OUT)
        GPIO.setup(self.GPIO_RF, GPIO.OUT)
        GPIO.setup(self.GPIO_RB, GPIO.OUT)
        return

    def turn_left(self):
        # set left backwards and right forwards
        # accept time of rotation as input
        GPIO.output(self.GPIO_LB, GPIO.HIGH)
        GPIO.output(self.GPIO_RF, GPIO.HIGH)
        return

    def turn_right(self):
        # set right backwards and left forwards
        # accept time of rotation as input
        GPIO.output(self.GPIO_LF, GPIO.HIGH)
        GPIO.output(self.GPIO_RB, GPIO.HIGH)
        return

    def move_forward(self):
        # set both forwards
        # accept x=time of movement as input
        GPIO.output(self.GPIO_LF, GPIO.HIGH)
        GPIO.output(self.GPIO_RF, GPIO.HIGH)
        return

    def move_backward(self):
        # set both backwards
        # accept time of movement as input
        GPIO.output(self.GPIO_LB, GPIO.HIGH)
        GPIO.output(self.GPIO_RB, GPIO.HIGH)
        return

    def stop(self):
        GPIO.output(self.GPIO_LB, GPIO.LOW)
        GPIO.output(self.GPIO_RB, GPIO.LOW)
        GPIO.output(self.GPIO_LF, GPIO.LOW)
        GPIO.output(self.GPIO_RF, GPIO.LOW)