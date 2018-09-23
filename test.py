# This is the SMARS Library test program
# it can be used to test each of the SMARS Library functions
#
# Written by Kevin McAleer
# September 2018

import SMARS_Library
from SMARS_Library import SmarsRobot
import time

# create an instance of the Smars Robot class
sm = SmarsRobot()

# set the robot type to 'quad'
sm.type = "quad"

def check_legs():
    key = ""
    print "Checking each leg - it should rotate to its full extent"
    key = raw_input("press a key to continue")

    print "front left leg"
    sm.legs[left_leg_front].up()
    key = raw_input("press a key to continue")

    print "front right leg"
    sm.legs[right_leg_front].up()
    key = raw_input("press a key to continue")

    print "back left leg"
    sm.legs[left_leg_back].up()
    key = raw_input("press a key to continue")

    print "back right leg"
    sm.legs[right_leg_back].up()
    key = raw_input("press a key to continue")

    print "Now moving each let to its default position."
    sm.legs[left_leg_front].setDefault()
    sm.legs[right_leg_front].setDefault()
    sm.legs[left_leg_back].setDefault()
    sm.legs[right_leg_back].setDefault()

def check_feet():
    print "Checking each foot - each foot should rise up."


# set the input choice to nothing
key = ""

# Display the main menu
while key != "q":
    print "SMARS QUAD TEST PROGRAM"
    print "-----------------------"
    print ""
    print "1) Set all limbs and feet to their default position"
    print "2) Set all feet to stand position"
    print "3) Set all feet to sit position"
    print "4) Check each limb is set correctly"

    key = raw_input("type an option, or type 'q' to quit ")
    if key == "1":
        for n in sm.legs:
            print n.name
            n.setDefault()
        for n in sm.feet:
            print n.name
            n.setDefault()
    if key == "2":
        for n in sm.feet:
            n.up()
    if key == "3":
        for n in sm.feet:
            n.down()
    if key == "4":
        check_legs()
        check_feet()

    if key == "q":
        print "Good bye!"
