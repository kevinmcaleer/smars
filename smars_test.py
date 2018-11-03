# smars_test.py
#
# Purpose: A simple test program for a standard SMARS
#
# Written by Kevin McAleer
# November 2018

import SMARS_Library as sl
from SMARS_Library import SmarsRobot
from SMARS_Library import leg
import time

# create an instance of the Smars Robot class
sm = SmarsRobot()
sm.setName("Rover")

# set the robot type to 'quad'
sm.type = "wheel"

print "SMARS TEST"
print "----------"
