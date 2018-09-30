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
sleep_count = 0.25 # the amount of time to wait between pwm operations

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
    def __init__(self,name=None, channel=None, leg_minAngle=None, leg_maxAngle=None, invert=None):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        # print "setting up leg object"
        self.name = name
        self.channel = channel
        self.leg_minAngle = leg_minAngle
        self.leg_maxAngle = leg_maxAngle
        self.invert = invert
        # self.leg_min = leg_min
        # self.leg_max = leg_max
        # print self.name
        # print self.channel
        # print "setting to up position"

        # Need to configure the in and max position for each limb
        # pwm.set_pwm(self.channel,self.channel,servo_max)
        time.sleep(sleep_count)

    def setDefault(self):
        self.setAngle(self.leg_maxAngle - self.leg_minAngle)

    def setBody(self):
        # Sets the limb to its default position.
        if self.invert == False:
            self.setAngle(self.leg_minAngle)
        else:
            self.setAngle(self.leg_maxAngle)

    def setStretch(self):
        # Sets the limb to its stretch position.
        if self.invert == False:
            self.setAngle(self.leg_minAngle)
        else:
            self.setAngle(self.leg_maxAngle)

    def setSwing(self):
        # Sets the limb to its stretch position.
        a = 0
        # print "Max Angle", self.leg_maxAngle, "Min angle", self.leg_minAngle, "Invert:", self.invert
        if self.invert == False:
            a = (self.leg_minAngle / 2) + self.leg_minAngle
            # print "INVERT = FALSE angle calculation is", a
            self.setAngle(a)
        else:
            a =(self.leg_maxAngle - self.leg_minAngle) / 2
            # print "INVERT = TRUE angle calculation is", a
            self.setAngle(a)
        # self.setAngle(self.leg_maxAngle - self.leg_minAngle / 2 )

    def up(self):
        if self.invert == False:
            self.setAngle(self.leg_minAngle)
        else:
            self.setAngle(self.leg_maxAngle)
        # time.sleep(sleep_count)

    def down(self):
        if self.invert == False:
            self.setAngle(self.leg_maxAngle)
        else:
            self.setAngle(self.leg_minAngle)
        # time.sleep(sleep_count)
        # print 'setting leg' , self.name , 'to down'

    def middle(self):
        self.setAngle(self.leg_maxAngle - self.leg_minAngle)
        # pwm.set_pwm(self.channel,self.channel,self.leg_min - self.leg_max)
        time.sleep(sleep_count)

    def show(self):
        print self.channel
        print self.name

    def moveTo(self, position):
        pwm.set_pwm(self.channel, self.channel, position)
        time.sleep(sleep_count)

    def setAngle(self, angle):
        # Works out the value of the angle by mapping the leg_min and leg_max to between 0 and 180 degrees
        print "Angle is:", angle

        pulse = 0

        # Check the angle is within the boundaries for this limb
        if angle >= self.leg_minAngle and angle <= self.leg_maxAngle:

            mapMax = self.leg_max - self.leg_min
            percentage = ( float(angle) / 180 ) * 100
            pulse = int( (( float(mapMax) / 100 ) * float(percentage) ) + self.leg_min)
            # print "Angle = ", angle
            # print "Angle as a percentage = ", percentage
            # print "pulse = ", pulse
            # print "map Max = ", mapMax
            # return pulse
            pwm.set_pwm(self.channel, self.channel, pulse)
        else:
            print "Error angle was outside of bounds for this leg: ", self.name, angle, "Minimum:", self.leg_minAngle, "Maximum:", self.leg_maxAngle

class SmarsRobot(object):

    def __init__(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

    # defines if the robot is a quad or wheel based robot
    # need to make this an enum then set the type to be one of the items in the list
    type = ['wheel', 'quad']

    # newLeg = leg()
    legs = []
    feet = []

    # add each foot to the feet array
    feet.append(leg(name = 'left_foot_front', channel = 1, leg_minAngle = 50,   leg_maxAngle = 150,  invert = False))
    feet.append(leg(name = 'left_foot_back',  channel = 3, leg_minAngle = 50,  leg_maxAngle = 150, invert = True))
    feet.append(leg(name = 'right_foot_front',channel = 7, leg_minAngle = 50, leg_maxAngle = 150, invert = True))
    feet.append(leg(name = 'right_foot_back', channel = 5, leg_minAngle = 50, leg_maxAngle = 150, invert = False))

    # add each leg to the legs array
    legs.append(leg(name = 'left_leg_front',  channel = 0, leg_minAngle = 0, leg_maxAngle = 90, invert = True))
    legs.append(leg(name = 'left_leg_back',   channel = 2, leg_minAngle = 90, leg_maxAngle = 180, invert = False))
    legs.append(leg(name = 'right_leg_front', channel = 6, leg_minAngle = 90, leg_maxAngle = 180, invert = False))
    legs.append(leg(name = 'right_leg_back',  channel = 4, leg_minAngle = 0, leg_maxAngle = 90, invert = True))
    # print "number of legs", len(legs)

    def leg_reset(self):
        for l in self.legs:
            l.setDefault()

        # self.legs("left_foot_front").moveTo(self.leg_max)
        # self.legs("left_foot_back").moveTo(self.leg_min)
        # self.legs("right_foot_front").moveTo(self.leg_max)
        # self.legs("right_foot_back").moveTo(self.leg_min)

    def middle(self):
        print "received middle command"
        for l in self.legs:
            l.middle()
            # l.show()

    def sit(self):
        print "received sit command"
        for l in self.feet:
            l.down()

    def stand(self):
        for l in self.feet:
            l.up()

    def walk(self):
        global left_leg_front
        global left_leg_back
        global right_leg_front
        global right_leg_back
        global left_foot_front
        global left_foot_back
        global right_foot_front
        global right_foot_back
        # Set all legs to up (sit)

        self.sit()
        time.sleep(sleep_count)

        # Set all legs to middle position
        self.middle()
        time.sleep(sleep_count)

        # Set all legs to down position (stand)
        self.stand()
        time.sleep(sleep_count)

        while True:

            # lift the other feet up
            print "Step 1"
            self.feet[left_foot_front].up()
            self.feet[right_foot_back].up()
            time.sleep(sleep_count)


            # set the front right and back left to half of stetch position
            print "Step 2"
            # print "about the set legs[left_leg_front]", left_leg_front, "setSwing"
            self.legs[left_leg_front].setSwing()
            # print "about the set legs[right_leg_back]", right_leg_back, "setSwing"
            self.legs[right_leg_back].setSwing()

            time.sleep(sleep_count)


            # put the feet down
            print "Step 3"
            self.feet[left_foot_front].down()
            self.feet[right_foot_back].down() #
            time.sleep(sleep_count)


            # set the front right back leg to body position
            print "Step 4"
            self.legs[left_leg_front].setBody()
            self.legs[right_leg_back].setBody() #
            time.sleep(sleep_count)

            ### Walk Cycle
            # lift the other feet up
            print "Step 5"
            self.feet[right_foot_front].up()
            self.feet[left_foot_back].up() #
            time.sleep(sleep_count)


            # set the front right and back left to half of stetch position
            print "Step 6"
            self.legs[right_leg_front].setSwing()
            self.legs[left_leg_back].setSwing() #
            time.sleep(sleep_count)


            # put the feet down
            print "Step 7"
            self.feet[right_foot_front].down()
            self.feet[left_foot_back].down() #
            time.sleep(sleep_count)


            # set the front right back leg to body position
            print "Step 8"
            self.legs[right_leg_front].setBody()
            self.legs[left_leg_back].setBody() #
            time.sleep(sleep_count)
