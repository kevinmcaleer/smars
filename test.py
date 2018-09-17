import SMARS_Library
from SMARS_Library import SmarsRobot

sm = SmarsRobot()

#  Telling sm to Sit

print "SMARS QUAD TEST PROGRAM"
sm.type = "quad"
sm.leg_reset()

key = raw_input("Press any key to sit down")
sm.sit()

key = raw_input("Press any key to stand")
sm.stand()
