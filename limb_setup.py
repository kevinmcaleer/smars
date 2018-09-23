#Leg setup

# setup leg 1:

from SMARS_Library import leg

def menu():
    print "Menu"
    print "----"
    print ""
    print "1) select channel"
    print "2) select angle"
    print "0) quit"
    print ""

def select_channel():
    global channel_number
    print "Select Channel"
    print "--------------"
    print ""
    print "currently selected channel is:", channel_number
    key = ""

    while channel_number <= 15:
            key = raw_input("type channel number:")
            channel_number = int(key)
            if channel_number >= 15:
                print "you typed", key, channel_number
                print "sorry that channel number is too high, needs to be between 0 and 15"
    l1.channel = channel_number

def select_angle():
    global angle
    print "Select Angle"
    print "------------"
    print ""
    print "current angle is:", angle

    # l1.setAngle(angle)
    key = ""
    while key != "q":
        key = raw_input("Type angle to set servo to, or press q to exit")
        print key
        if key == "q":
            print ""
        else:
            # if raw_input ==
            # angle = angle + 10
            angle = int(key)
            l1.setAngle(angle)
            print "current angle:", angle

#globals
angle = 0
channel_number = 0
l1 = leg()
l1.name = "left_leg_front"
l1.channel = channel_number
l1.leg_minAngle = 0
l1.leg_maxAngle = 180
l1.invert = False

menu_key = ""
# show Menu until quit
while menu_key != "0":
    menu()
    print "current channel is:", l1.channel
    print "current angle is:", angle
    menu_key = raw_input("enter number ")

    if menu_key == "1":
        select_channel()
    if menu_key == "2":
        select_angle()
    if menu_key == "0":
        print "Good bye!"
