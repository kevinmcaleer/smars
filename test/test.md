# Unit Tests

## def set_servo_pulse(channel, pulse):
1. Check that channel is a positive integer (between 0 and 15)
1. Check that pulse is a number between 0 and 4096

# Class leg()
## def moveTo(self, position):
check that position is valid

## def setAngle(self, angle):
check that angle is between 0 and 180

# class SmarsRobot(object):

## def setName(self, name
check that name doesn't exceed 20 characters

## def walkForward(self, steps):
check that steps is a valid integer, and is less than 100

## def walkBackward(self, steps):
check that steps is a valid integer, and is less than 100

## def clap(self, clap_count):
check that clap_count is less than 100

##  def wiggle(self, wiggle_count):
check that wiggle_count is less than 100
