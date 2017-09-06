import unittest
import datetime
from babysitter import *

class TestBabysitter(unittest.TestCase):

    def setUp(self):
        self.babysitter = Babysitter()

    def test_babysitter_starts_no_earlier_than_5PM(self):
        self.assertRaises(StartsTooEarly, self.babysitter.job_starts_at, start_time = datetime.time(16))

    def test_babysitter_sets_start_time_when_it_is_not_earlier_than_5PM(self):
        start_time = datetime.time(17)
        self.babysitter.job_starts_at(start_time)
        self.assertEqual(self.babysitter.start_time, start_time)

    def test_babysitter_sets_start_time_when_it_is_after_midnight_and_before_4AM(self):
        start_time = datetime.time(1)
        self.babysitter.job_starts_at(start_time)
        self.assertEqual(self.babysitter.start_time, start_time)

    def test_babysitter_start_time_must_be_before_end_time(self):
        self.babysitter.job_ends_at(datetime.time(18))
        self.assertRaises(StartTimeAfterEndTime, self.babysitter.job_starts_at, start_time = datetime.time(19))

    def test_babysitter_ends_no_later_than_4AM(self):
        self.assertRaises(EndsTooLate, self.babysitter.job_ends_at, end_time = datetime.time(5))

    def test_babysitter_ends_no_later_than_4AM_but_accepts_17_to_midnight(self):
        end_time = datetime.time(17)
        self.babysitter.job_ends_at(end_time)
        self.assertEqual(self.babysitter.end_time, end_time)
        end_time = datetime.time(23)
        self.babysitter.job_ends_at(end_time)
        self.assertEqual(self.babysitter.end_time, end_time)

    def test_babysitter_sets_end_time_when_it_is_not_later_than_4AM(self):
        end_time = datetime.time(4)
        self.babysitter.job_ends_at(end_time)
        self.assertEqual(self.babysitter.end_time, end_time)

    def test_bedtime_must_be_between_start_time_and_end_time(self):
        self.babysitter.job_starts_at(datetime.time(17))
        self.babysitter.job_ends_at(datetime.time(19))
        self.assertRaises(InvalidBedtime, self.babysitter.bedtime_is, bedtime=datetime.time(20))

    def test_babysitter_sets_bedtime_when_it_is_between_start_and_end_times(self):
        self.babysitter.job_starts_at(datetime.time(17))
        self.babysitter.job_ends_at(datetime.time(19))
        bedtime = datetime.time(18)
        self.babysitter.bedtime_is(bedtime)
        self.assertEqual(self.babysitter.bedtime, bedtime)

    def test__is_invalid_start_time(self):
        self.assertTrue(self.babysitter._is_invalid_start_time(datetime.time(16)))
        self.assertTrue(self.babysitter._is_invalid_start_time(datetime.time(5)))
        self.assertFalse(self.babysitter._is_invalid_start_time(datetime.time(17)))
        self.assertFalse(self.babysitter._is_invalid_start_time(datetime.time(0)))


if __name__ == '__main__':
    unittest.main()