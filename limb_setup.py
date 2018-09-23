#Leg setup

# setup leg 1:

from SMARS_Library import leg

l1 = leg()
l1.name = "left_leg_front"
l1.channel = 15
l1.leg_minAngle = 0
l1.leg_maxAngle = 180
l1.invert = False

# print "setting minimum position"
angle = 0
l1.setAngle(angle)
key = ""
while key != "0":
    key = raw_input("setting min position, press 0 to exit")
    print key
    # if raw_input ==
    angle = angle + 10
    l1.setAngle(angle)
    print "current angle:", angle
