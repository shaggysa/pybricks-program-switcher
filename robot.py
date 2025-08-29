from pybricks.hubs import *
from pybricks.robotics import *
from pybricks.pupdevices import *
from pybricks.parameters import *

HUB = PrimeHub()

#Adjust these parameters to fit your robot. Also ensure that you add any sensors here.

LEFT_DRIVE = Motor(Port.A, Direction.COUNTERCLOCKWISE)
RIGHT_DRIVE = Motor(Port.B, Direction.CLOCKWISE)
LEFT_ATTACHMENT = Motor(Port.C, Direction.COUNTERCLOCKWISE)
RIGHT_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)

DRIVE_BASE = DriveBase(LEFT_DRIVE, RIGHT_DRIVE, 50, 100)
COLOR_SENSOR = ColorSensor(Port.E)