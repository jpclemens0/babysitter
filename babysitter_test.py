import unittest
import datetime
from babysitter import *
from babysitter_time import *

class TestBabysitter(unittest.TestCase):

    def setUp(self):
        self.babysitter = Babysitter()

    def test_babysitter_starts_no_earlier_than_5PM(self):
        self.assertRaises(StartsTooEarly, self.babysitter.job_starts_at, start_time = 16)

    def test_babysitter_sets_start_time_when_it_is_not_earlier_than_5PM(self):
        self.babysitter.job_starts_at(17)
        self.assertEqual(self.babysitter.start_time, BabysitterTime(17))

    def test_babysitter_sets_start_time_when_it_is_after_midnight_and_before_4AM(self):
        self.babysitter.job_starts_at(1)
        self.assertEqual(self.babysitter.start_time, BabysitterTime(1))

    def test_babysitter_start_time_must_be_before_end_time(self):
        self.babysitter.job_ends_at(18)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter.job_starts_at, start_time = 19)

    def test_babysitter_ends_no_later_than_4AM(self):
        self.assertRaises(EndsTooLate, self.babysitter.job_ends_at, end_time = 5)

    def test_babysitter_ends_no_later_than_4AM_but_accepts_5PM_to_midnight(self):
        self.babysitter.job_ends_at(17)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(17))
        self.babysitter.job_ends_at(23)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(23))

    def test_babysitter_sets_end_time_when_it_is_not_later_than_4AM(self):
        self.babysitter.job_ends_at(4)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(4))

    def test_babysitter_end_time_must_be_after_start_time(self):
        self.babysitter.job_starts_at(20)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter.job_ends_at, 18)

    def test_babysitter_sets_bedtime_for_any_time(self):
        self.babysitter.bedtime_is(7)
        self.assertEqual(self.babysitter.bedtime, BabysitterTime(7))

    def test__is_invalid_time(self):
        self.assertTrue(self.babysitter._is_invalid_time(16))
        self.assertTrue(self.babysitter._is_invalid_time(5))
        self.assertFalse(self.babysitter._is_invalid_time(17))
        self.assertFalse(self.babysitter._is_invalid_time(0))

    def test__is_start_time_after_end_time(self):
        self.babysitter.job_ends_at(20)
        self.assertTrue(self.babysitter._is_start_time_after_end_time(21))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(1))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(18))

        self.babysitter.job_ends_at(2)
        self.assertTrue(self.babysitter._is_start_time_after_end_time(3))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(20))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(1))

    def test__is_end_time_before_start_time(self):
        self.babysitter.job_starts_at(20)
        self.assertFalse(self.babysitter._is_end_time_before_start_time(21))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(1))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(18))

        self.babysitter.job_starts_at(2)
        self.assertFalse(self.babysitter._is_end_time_before_start_time(3))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(20))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(1))

    def test__is_valid_start_time(self):
        self.assertRaises(StartsTooEarly, self.babysitter._is_valid_start_time, 16)
        self.babysitter.job_ends_at(18)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter._is_valid_start_time, 19)
        self.assertTrue(self.babysitter._is_valid_start_time(17))

    def test__is_valid_end_time(self):
        self.assertRaises(EndsTooLate, self.babysitter._is_valid_end_time, 5)
        self.babysitter.job_starts_at(20)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter._is_valid_end_time, 18)
        self.assertTrue(self.babysitter._is_valid_end_time(21))


if __name__ == '__main__':
    unittest.main()