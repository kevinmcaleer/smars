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
# import logging
# logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
sleep_count = 0.5 # the amount of time to wait between pwm operations

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

    def __init__(self,name=None, channel=None):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        print "setting up leg object"
        self.name = name
        self.channel = channel
        print self.name
        print self.channel
        print "setting to up position"
        pwm.set_pwm(self.channel,self.channel,servo_max)
        time.sleep(sleep_count)

    def up(self):
        pwm.set_pwm(self.channel,self.channel,servo_max)
        time.sleep(sleep_count)

    def down(self):
        pwm.set_pwm(self.channel, self.channel,servo_min)
        time.sleep(sleep_count)
        print 'setting leg' , self.name , 'to down'

    def middle(self):
        pwm.set_pwm(self.channel,self.channel,servo_min - servo_max)
        time.sleep(sleep_count)

    def show(self):
        print self.channel
        print self.name

class SmarsRobot(object):

    def __init__(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

    # defines if the robot is a quad or wheel based robot
    # need to make this an enum then set the type to be one of the items in the list
    type = ['wheel', 'quad']

    # newLeg = leg()
    legs = []
    legs.append(leg(name = 'left_foot_front', channel = 0))
    legs.append(leg(name = 'left_foot_back',channel = 3))
    legs.append(leg(name = 'right_foot_front',channel = 6))
    legs.append(leg(name = 'right_foot_back',channel = 5))
    print "number of legs", len(legs)

    # setup legs and feet to correspond to the correct channel
    left_leg_front   = 0
    left_foot_front  = 1
    left_leg_back    = 2
    left_foot_back   = 3
    right_leg_front  = 6
    right_foot_front = 7
    right_leg_back   = 4
    right_foot_back  = 5

    def middle(self):
        for l in self.legs:
            l.middle()
            l.show()

    def sit(self):
        print "received sit command"
        for l in self.legs:
            # print "sitting down leg: ", l.name
            l.down()
        # self.legs["left_leg_front"].down()
        # self.legs["left_leg_front"].down()
        # self.legs['right_leg_back'].down()
        # self.legs['right_leg_front'].down()
