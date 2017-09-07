import unittest
import datetime
from babysitter_time import *

class TestBabysitterTime(unittest.TestCase):

    def test_set_time_between_5PM_and_midnight(self):
        self.time = BabysitterTime(17)
        self.assertEqual(self.time.time, datetime.datetime.combine(datetime.date.today(), datetime.time(17)))

    def test_set_time_between_midnight_and_5PM(self):
        self.time = BabysitterTime(1)
        self.assertEqual(self.time.time, datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days = 1), datetime.time(1)))

    def test_lt(self):
        self.assertTrue(BabysitterTime(1) < BabysitterTime(2))
        self.assertTrue(BabysitterTime(17) < BabysitterTime(18))
        self.assertTrue(BabysitterTime(17) < BabysitterTime(16))
        self.assertTrue(BabysitterTime(23) < BabysitterTime(0))

    def test_gt(self):
        self.assertTrue(BabysitterTime(2) > BabysitterTime(1))
        self.assertTrue(BabysitterTime(18) > BabysitterTime(17))
        self.assertTrue(BabysitterTime(16) > BabysitterTime(17))
        self.assertTrue(BabysitterTime(0) > BabysitterTime(23))