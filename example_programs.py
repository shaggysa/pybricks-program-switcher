from pybricks.tools import wait
from robot import *

def drive_forever():
    while True:
        DRIVE_BASE.drive(500, 0)

def turn_left_90():
    DRIVE_BASE.turn(90)

def turn_right_90():
    DRIVE_BASE.turn(-90)

def drive_5_seconds():
    DRIVE_BASE.drive(500)
    wait(5000)
    DRIVE_BASE.brake()



