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

