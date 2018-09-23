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

    key = raw_input("type an option and press enter")
    if key == "1":
        for n in sm.legs:
            print n.name
            n.setDefault()
    if key == "2":
        for n in sm.legs:
            n.up()
    if key == "3":
        for n in sm.legs:
            n.down()
    if key == "q":
        print "Good bye!"
