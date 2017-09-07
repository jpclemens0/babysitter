import unittest
import datetime
from babysitter_time import *

class TestBabysitterTime(unittest.TestCase):

    def setUp(self):
        self.time = BabysitterTime()

    def test_set_time_between_5PM_and_midnight(self):
        self.time.set(17)
        self.assertEqual(self.time.time, datetime.datetime.combine(datetime.date.today(), datetime.time(17)))

