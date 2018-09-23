#Leg setup

# setup leg 1:

from SMARS_Library import leg

#globals
angle = 0
channel_number = 0

def menu():
    print "Menu"
    print "----"
    print ""
    print "1) select channel"
    print "2) select angle"
    print "0) quit"
    print ""

def select_channel():
    print "Select Channel"
    print "--------------"
    print ""
    print "currently selected channel is:", channel_number

    while channel_number <= 15:
            channel_number = raw_input("type channel number:")
            if channel_number >= 15:
                print "sorry that channel number is too high, needs to be between 0 and 15"
    return channel_number
def select_angle():
    l1.setAngle(angle)
    key = ""
    while key != "0":
        key = raw_input("setting min position, press 0 to exit")
        print key
        # if raw_input ==
        angle = angle + 10
        l1.setAngle(angle)
        print "current angle:", angle

l1 = leg()
l1.name = "left_leg_front"
l1.channel = 15
l1.leg_minAngle = 0
l1.leg_maxAngle = 180
l1.invert = False

# show Menu until quit
while menu_key != "0":
    menu()
    print "current channel is:", l1.channel
    print "current angle is:", angle
    menu_key = raw_input("enter number ")

    if menu_key == "1":
        l1.channel = select_channel()
    if menu_key == "2":
        select_angle()
    if menu_key == "0":
        print "Good bye!"
