#Leg setup

VERSION = "1.0"
# setup leg 1:

# from SMARS_Library import *
from smars_library.smars_library import SmarsRobot, Leg
import smars_library.smars_library

channel_number = 1
l1 = Leg(name="limb test", channel=channel_number,  leg_minangle=0, leg_maxangle=180, invert=False)
# l1.name = "left_leg_front"
# l1.channel = channel_number
# l1.leg_minAngle = 0
# l1.leg_maxAngle = 180
# l1.invert = False

def menu():
    """ display the main menu """
    print("")
    print("*** SMARS Limb setup, Version ", VERSION, "***")
    print("")
    print("Menu")
    print("----")
    print("") 
    print("Select:")
    print("1) Channel")
    print("2) Angle")
    print("0) Quit")
    print("")

channel_number = 0
def select_channel():
    global channel_number
    global l1
    print("")
    print("")
    print("CHANNEL")
    print("-------------------------")
    print("")
    print("Currently selected channel is:", channel_number)
    print("")
    print("Select new channel.")
    key = ""
    ch = 0
    #  need to make this loop exit once the channel number is selected and "q" pressed
    while key != "q":
        key = input("Type channel number:, or q to return to the main menu")
        print("")
        print(key)
        if key == "q":
            print("")
        else:
            ch = int(key)
            if ch >= 16:
                print("sorry that channel number is too high, needs to be between 0 and 15")
            else:
                channel_number = int(ch)
                l1.channel = channel_number
                l1.show()

angle = 0

def show_status():
    """
    Shows the currently selected channel and angle
    """
    print("")
    print("[current channel is:", l1.channel,"]:[current angle is:", angle,"]")
    print("")

def select_angle():
    """ change the current angle """
    global angle
    print("Select Angle")
    print("------------")
    print("")
    print("current angle is:", angle)

    # l1.setAngle(angle)
    key = ""
    while key != "q":
        key = input("Type angle to set servo to, or press q to exit")
        print(key)
        if key == "q":
            print("")
        else:
            # if raw_input ==
            # angle = angle + 10
            angle = int(key)
            l1.setangle(angle)
            print("current angle:", angle)

menu_key = ""
# show Menu until quit
while menu_key != "0":
    menu()
    show_status()
    menu_key = input("enter choice ")

    if (menu_key == "1") or (menu_key == "c"):
        select_channel()
    if (menu_key == "2") or (menu_key == "a"):
        select_angle()
    if (menu_key == "0") or (menu_key == "q"):
        print("Good bye!")
