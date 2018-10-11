# SMARS Python library
# Kevin McAleer September 2018
# Purpose: Provides library routines for the SMARS robot and quad robots

#
#You will need to install the following python libraries for this to work:
#
  # sudo apt-get install python-smbus
  # sudo apt-get install i2c-tools

# You will also need to enable the I2C interface using the raspberry pi configuration tool (raspi-config)

# You will need ot install the adafruit PCA9685 servo driver python library

# If you have Raspbian, not Occidentalis check /etc/modprobe.d/raspi-blacklist.conf and comment "blacklist i2c-bcm2708" by running sudo nano /etc/modprobe.d/raspi-blacklist.conf and adding a # (if its not there).
# If you're running Wheezy or something-other-than-Occidentalis, you will need to
# add the following lines to /etc/modules
# i2c-dev
# i2c-bcm2708

import Adafruit_PCA9685
import time
# from __future__ import division
# import logging
# logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
sleep_count = 0.05 # the amount of time to wait between pwm operations

# setup legs and feet to correspond to the correct channel
left_leg_front   = 0 # channel 0
left_leg_back    = 1 # channel 2
right_leg_front  = 2 # channel 6
right_leg_back   = 3 # channel 4

left_foot_front  = 0 # channel 1
left_foot_back   = 1 # channel 3
right_foot_front = 2 # channel 7
right_foot_back  = 3 # channel 5

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

class leg(object):

    leg_min = 150
    leg_max = 600
    swingAngle = 0
    bodyAngle = 0
    stretchAngle = 0
    currentAngle = 0

    def __init__(self,name=None, channel=None, leg_minAngle=None, leg_maxAngle=None, invert=None):
        # Initialises the leg object
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        # print "setting up leg object"
        self.name = name
        self.channel = channel
        self.leg_minAngle = leg_minAngle
        self.leg_maxAngle = leg_maxAngle
        self.invert = invert

        if self.invert == False:
            self.bodyAngle = self.leg_minAngle
            self.stretchAngle = self.leg_maxAngle
            self.swingAngle = (self.leg_minAngle / 2) + self.leg_minAngle
        else:
            self.bodyAngle = self.leg_maxAngle
            self.stretchAngle = self.leg_minAngle
            self.swingAngle = (self.leg_maxAngle - self.leg_minAngle) / 2
        self.currentAngle = self.bodyAngle

    def setDefault(self):
        # Sets the limb to the default angle, by dividing the maximum and minimum angles that were set previously
        self.setAngle(self.leg_maxAngle - self.leg_minAngle)
        self.currentAngle = self.leg_maxAngle - self.leg_minAngle

    def setBody(self):
        # Sets the limb to its body position.
        if self.invert == False:
            self.setAngle(self.leg_minAngle)
            self.bodyAngle = self.leg_minAngle
        else:
            self.setAngle(self.leg_maxAngle)
            self.bodyAngle = self.leg_maxAngle
        self.currentAngle = self.bodyAngle

    def setStretch(self):
        # Sets the limb to its stretch position.
        if self.invert == False:
            self.setAngle(self.leg_maxAngle)
            self.stretchAngle = self.leg_maxAngle
        else:
            self.setAngle(self.leg_minAngle)
            self.stretchAngle = self.leg_minAngle
        self.currentAngle = self.stretchAngle

    def setSwing(self):
        # Sets the limb to its swing position, which is 45 degrees - halfway between the body and stretch position.
        a = 0
        # print "Max Angle", self.leg_maxAngle, "Min angle", self.leg_minAngle, "Invert:", self.invert
        if self.invert == False:
            a = (self.leg_minAngle / 2) + self.leg_minAngle
            self.setAngle(a)
        else:
            a =(self.leg_maxAngle - self.leg_minAngle) / 2
            self.setAngle(a)
        self.swingAngle = a
        self.currentAngle = self.swingAngle

    def up(self):
        # raises the limb to its minimum angle
        if self.invert == False:
            self.setAngle(self.leg_minAngle)
        else:
            self.setAngle(self.leg_maxAngle)

    def down(self):
        # lowers the limb to its maximum angle
        if self.invert == False:
            self.setAngle(self.leg_maxAngle)
        else:
            self.setAngle(self.leg_minAngle)

    def middle(self):
        #  moves the limb to half way between up and down.
        self.setAngle(self.leg_maxAngle - self.leg_minAngle)

    def show(self):
        # used for debugging - shows the servo driver channel number and the limb name
        print self.channel
        print self.name

    def moveTo(self, position):
        # obsolete - use setAngle instead
        pwm.set_pwm(self.channel, self.channel, position)
        time.sleep(sleep_count)

    def setAngle(self, angle):
        # Works out the value of the angle by mapping the leg_min and leg_max to between 0 and 180 degrees
        # Then moves the limb to that position
        pulse = 0

        # Check the angle is within the boundaries for this limb
        if angle >= self.leg_minAngle and angle <= self.leg_maxAngle:
            mapMax = self.leg_max - self.leg_min
            percentage = ( float(angle) / 180 ) * 100
            pulse = int( (( float(mapMax) / 100 ) * float(percentage) ) + self.leg_min)

            # send the servo the pulse, to set the angle
            pwm.set_pwm(self.channel, self.channel, pulse)
        else:
            # display an error message if the angle set was outside the range (leg_minAngle and leg_maxAngle)
            print "Warning: angle was outside of bounds for this leg: ", self.name, angle, "Minimum:", self.leg_minAngle, "Maximum:", self.leg_maxAngle
        self.currentAngle = angle

    def untick(self):
        # TODO - need to change the values for walking backwards
        # Used to walk backwards
        if self.name == "left_leg_front" or self.name == "left_leg_back":
            if self.currentAngle <= self.leg_maxAngle:
                self.currentAngle += 2
                # print self.name, "setting angle to ", self.currentAngle
                self.setAngle(self.currentAngle)
                return False
            else:

                return True
        elif self.name == "right_leg_front" or self.name == "right_leg_back":
            if self.currentAngle >= self.leg_minAngle:
                self.currentAngle -= 2
                # print self.name, "setting angle to ", self.currentAngle
                self.setAngle(self.currentAngle)
                return False
            else:
                # print "angle met:", self.currentAngle, "max angle:", self.leg_maxAngle, "min angle:", self.leg_minAngle
                return True

    def tick(self):
        # Used for walking forward.
        # Each tick received changes the current angle of the limb, unless an limit is reached, which then returns a true value
        if self.name == "left_leg_front" or self.name == "left_leg_back":
            if self.currentAngle <= self.leg_maxAngle:
                self.currentAngle += 2
                # print self.name, "setting angle to ", self.currentAngle
                self.setAngle(self.currentAngle)
                return False
            else:
                # print "angle met:", self.currentAngle
                return True
        elif self.name == "right_leg_front" or self.name == "right_leg_back":
            if self.currentAngle >= self.leg_minAngle:
                self.currentAngle -= 2
                # print self.name, "setting angle to ", self.currentAngle
                self.setAngle(self.currentAngle)
                return False
            else:
                # print "angle met:", self.currentAngle, "max angle:", self.leg_maxAngle, "min angle:", self.leg_minAngle
                return True

class SmarsRobot(object):
# This is used to model the robot, its legs and its sensors
    def __init__(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

    # defines if the robot is a quad or wheel based robot
    # need to make this an enum then set the type to be one of the items in the list
    type = ['wheel', 'quad']

    # newLeg = leg()
    legs = []
    feet = []
    name = "" # the friendly name for the robot - used in console messages.

    # add each foot to the feet array
    feet.append(leg(name = 'left_foot_front', channel = 1, leg_minAngle = 50,   leg_maxAngle = 150,  invert = False))
    feet.append(leg(name = 'left_foot_back',  channel = 3, leg_minAngle = 50,  leg_maxAngle = 150, invert = True))
    feet.append(leg(name = 'right_foot_front',channel = 7, leg_minAngle = 50, leg_maxAngle = 150, invert = True))
    feet.append(leg(name = 'right_foot_back', channel = 5, leg_minAngle = 50, leg_maxAngle = 150, invert = False))

    # add each leg to the legs array
    legs.append(leg(name = 'left_leg_front',  channel = 0, leg_minAngle = 9, leg_maxAngle = 90, invert = True))
    legs.append(leg(name = 'left_leg_back',   channel = 2, leg_minAngle = 90, leg_maxAngle = 180, invert = False))
    legs.append(leg(name = 'right_leg_front', channel = 6, leg_minAngle = 90, leg_maxAngle = 180, invert = False))
    legs.append(leg(name = 'right_leg_back',  channel = 4, leg_minAngle = 9, leg_maxAngle = 90, invert = True))
    # print "number of legs", len(legs)

    def setName(self, name):
        # Sets the robots name, used for displaying console messages.
        self.name = name
        print "***", name, "Online ***"

    def leg_reset(self):
        # used to reset all the legs
        for l in self.legs:
            l.setDefault()

    def middle(self):
        # used to position all the legs into the middle position
        print "received middle command"
        for l in self.legs:
            l.middle()
            # l.show()

    def sit(self):
        # used to sit the robot down
        print self.name, "sitting Down."
        for l in self.feet:
            l.down()

    def stand(self):
        print self.name, "standing up."
        for l in self.feet:
            l.up()

    def turnLeft(self):
        global left_leg_front
        global left_leg_back
        global right_leg_front
        global right_leg_back
        global left_foot_front
        global left_foot_back
        global right_foot_front
        global right_foot_back
        print self.name, "Turning left."
        for f in self.feet:
            f.down()
        time.sleep(sleep_count)
        for l in self.legs:
            l.setSwing()
        time.sleep(sleep_count)

        # twist body
        self.legs[left_leg_front].setStretch()
        self.legs[left_leg_back].setBody()
        self.legs[right_leg_front].setBody()
        self.legs[right_leg_back].setStretch()
        time.sleep(sleep_count)

        # move legs one at a time back to swing position
        for l in range(0, 4):
            self.feet[l].down()
            time.sleep(l)
            self.legs[l].setSwing()
            time.sleep(l)
            self.feet[l].up()
            time.sleep(l)

    def walkForward(self, steps):
        # used to move the robot forward.

        # include the global variables
        global left_leg_front
        global left_leg_back
        global right_leg_front
        global right_leg_back
        global left_foot_front
        global left_foot_back
        global right_foot_front
        global right_foot_back

        # set the legs to the correct position for walking.
        self.sit()
        self.legs[left_leg_front].setBody()
        self.legs[left_leg_back].setBody()
        self.legs[right_leg_front].setSwing()
        self.legs[right_leg_back].setSwing()
        self.stand()

        # the walking cycle, loops for the number of steps provided.
        currentStep = 0;
        while currentStep < steps:
            currentStep += 1
            for n in range (0, 4):
                if self.legs[n].tick() == False:
                    # print self.name, "walking, step", currentStep, "of", steps
                    self.legs[n].tick()
                # while self.legs[n].tick() == False:
                #     #loop until limit reached then lift leg reset and lower leg.
                #     self.legs[n].tick()
                #
                #     time.sleep(sleep_count)
                else:
                    # print "moving leg:", self.legs[n].name
                    self.feet[n].down()
                    time.sleep(sleep_count)

                    # change this to left and right legs, rather than invert or not invert
                    if self.legs[n].invert == False:

                        if self.legs[n].name == "right_leg_front":

                            self.legs[n].setStretch()
                        else:

                            self.legs[n].setBody()
                    elif self.legs[n].invert == True:
                        if self.legs[n].name == "right_leg_back":

                            self.legs[n].setBody()
                        else:

                            self.legs[n].setStretch()
                    time.sleep(sleep_count)
                    self.feet[n].up()
                    time.sleep(sleep_count)
