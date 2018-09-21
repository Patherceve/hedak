#!/usr/bin/env python

import Adafruit_PCA9685
import math
import time

class Servo:
    
    #Constructor
    def __init__(self, channel, servo_min = 150, servo_max = 600, frequency = 60):
        self.channel = channel
        self.servo_min = servo_min
        self.servo_max = servo_max
        self.frequency = frequency
        
    def setup(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(self.frequency)
        
    def angle_to_pulse(self, val):
        oldRange = 180
        newRange = self.servo_max - self.servo_min
        return math.floor(((val * newRange) / oldRange) + self.servo_min)
        
    def setAngle(self, angle):
        if(angle < 0):
            angle = 0
        elif(angle > 180):
            angle = 180
        self.pwm.set_pwm(self.channel, 0, self.angle_to_pulse(angle))