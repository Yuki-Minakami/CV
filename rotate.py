#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import RPi.GPIO as GPIO
import time
import signal
import atexit
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.OUT, initial=False)
p = GPIO.PWM(35,50) #50HZ

p.start(0)

sleep(1)


def rotateA(duty):
    p.ChangeDutyCycle(duty)
    sleep(0.2)
    p.ChangeDutyCycle(0)
    sleep(2)

i=2.5
while i<10:
    rotateA(i)
    i=i+1

p.stop()

GPIO.cleanup()


