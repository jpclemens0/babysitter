import unittest
from babysitter_time import *


class TestBabysitterTime(unittest.TestCase):

    def test_set_time_between_5PM_and_midnight(self):
        self.time = BabysitterTime(17)
        self.assertEqual(self.time.time, datetime.datetime.combine(datetime.date.today(), datetime.time(17)))

    def test_set_time_with_hour_and_minute(self):
        self.time = BabysitterTime(17, 30)
        self.assertEqual(self.time.time, datetime.datetime.combine(datetime.date.today(), datetime.time(17, 30)))

    def test_set_time_between_midnight_and_5PM(self):
        self.time = BabysitterTime(1)
        self.assertEqual(self.time.time,
                         datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1),
                                                   datetime.time(1)))

    def test_lt(self):
        self.assertTrue(BabysitterTime(1) < BabysitterTime(2))
        self.assertTrue(BabysitterTime(17) < BabysitterTime(18))
        self.assertTrue(BabysitterTime(17) < BabysitterTime(16))
        self.assertTrue(BabysitterTime(23) < BabysitterTime(0))
        self.assertTrue(BabysitterTime(23) < BabysitterTime(23, 30))
        self.assertTrue(BabysitterTime(23, 30) < BabysitterTime(0))

    def test_gt(self):
        self.assertTrue(BabysitterTime(2) > BabysitterTime(1))
        self.assertTrue(BabysitterTime(18) > BabysitterTime(17))
        self.assertTrue(BabysitterTime(16) > BabysitterTime(17))
        self.assertTrue(BabysitterTime(0) > BabysitterTime(23))
        self.assertTrue(BabysitterTime(2, 30) > BabysitterTime(2))
        self.assertTrue(BabysitterTime(3) > BabysitterTime(2, 30))

    def test_eq(self):
        self.assertTrue(BabysitterTime(2) == BabysitterTime(2))
        self.assertTrue(BabysitterTime(2, 30) == BabysitterTime(2, 30))

    def test_minus(self):
        self.assertEqual(BabysitterTime(20) - BabysitterTime(18), datetime.timedelta(hours=2))
        self.assertEqual(BabysitterTime(2) - BabysitterTime(18), datetime.timedelta(hours=8))
        self.assertEqual(BabysitterTime(18) - BabysitterTime(2), datetime.timedelta(hours=-8))
        self.assertEqual(BabysitterTime(20, 30) - BabysitterTime(18), datetime.timedelta(hours=2, minutes=30))
        self.assertEqual(BabysitterTime(2) - BabysitterTime(18, 30), datetime.timedelta(hours=7, minutes=30))
        self.assertEqual(BabysitterTime(18, 30) - BabysitterTime(2), datetime.timedelta(hours=-8, minutes=30))
        self.assertEqual(BabysitterTime(20, 45) - BabysitterTime(18, 15), datetime.timedelta(hours=2, minutes=30))

    def test_full_hours_since(self):
        self.assertEqual(BabysitterTime(20).full_hours_since(BabysitterTime(17)), 3)
        self.assertEqual(BabysitterTime(20).full_hours_since(BabysitterTime(17, 30)), 2)
        self.assertEqual(BabysitterTime(20, 30).full_hours_since(BabysitterTime(17)), 3)
        self.assertEqual(BabysitterTime(20, 30).full_hours_since(BabysitterTime(17, 30)), 3)
        self.assertEqual(BabysitterTime(2).full_hours_since(BabysitterTime(17)), 9)
