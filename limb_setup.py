#Leg setup

# setup leg 1:

from SMARS_Library import leg

l1 = leg()
l1.name = "left_leg_front"
l1.channel = 1

# print "setting minimum position"
position = 300
l1.moveTo(position)
key = ""
while key != "0":
    key = raw_input("setting min position, press 0 to exit")
    print key
    # if raw_input ==
    position = position + 10
    l1.moveTo(position)
    print "current position:", position
