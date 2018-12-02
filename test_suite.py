import unittest
from SMARS_Library import leg

class setServoPulseTestCase(unittest.TestCase):
    """ tests setServoPulse """

    def test_setServoPulseChannelLessThan15(self):
        for channel in range(0,16):
            self.assertTrue(setServoPulse(channel))

    def test_setServoPulseIsNumberBetween0And4096():
        self.assertTrue(setServoPulse(0,0))
        self.assertTrue(setServoPulse(0,4096))
        self.assertTrue(setServoPulse(0,2000))
        self.assertFalse(setServoPulse(0,4097))

    
