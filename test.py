import SMARS_Library
from SMARS_Library import SmarsRobot
import time

sm = SmarsRobot()

#  Telling sm to Sit

print "SMARS QUAD TEST PROGRAM"
sm.type = "quad"

for n in sm.legs:
    print n.name
    n.setDefault()
    # n.down()
    time.sleep(1)
    # n.up()
    # time.sleep(1)
    key = raw_input("Press any key to sit down")


#  BUG In leg_reset code. cannot call an object by name from the list...
# sm.leg_reset()

key = raw_input("Press any key to sit down")
sm.sit()

key = raw_input("Press any key to stand")
sm.stand()
