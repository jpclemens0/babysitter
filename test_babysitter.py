import unittest
from babysitter import *
from babysitter_time import *


class TestBabysitter(unittest.TestCase):

    def setUp(self):
        self.babysitter = Babysitter()

    def test_babysitter_starts_no_earlier_than_5PM(self):
        self.assertRaises(StartsTooEarly, self.babysitter.job_starts_at, hour=16)
        self.assertRaises(StartsTooEarly, self.babysitter.job_starts_at, hour=16, minute=30)
        self.assertRaises(StartsTooEarly, self.babysitter.job_starts_at, hour=4, minute=1)

    def test_babysitter_sets_start_time_when_it_is_not_earlier_than_5PM(self):
        self.babysitter.job_starts_at(17)
        self.assertEqual(self.babysitter.start_time, BabysitterTime(17))
        self.babysitter.job_starts_at(17, 30)
        self.assertEqual(self.babysitter.start_time, BabysitterTime(17, 30))

    def test_babysitter_sets_start_time_when_it_is_after_midnight_and_not_later_than_4AM(self):
        self.babysitter.job_starts_at(1)
        self.assertEqual(self.babysitter.start_time, BabysitterTime(1))
        self.babysitter.job_starts_at(1, 30)
        self.assertEqual(self.babysitter.start_time, BabysitterTime(1, 30))
        self.babysitter.job_starts_at(4)
        self.assertEqual(self.babysitter.start_time, BabysitterTime(4))

    def test_babysitter_start_time_must_not_be_later_than_end_time(self):
        self.babysitter.job_ends_at(18)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter.job_starts_at, hour=19)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter.job_starts_at, hour=19, minute=30)
        self.babysitter.job_ends_at(18, 30)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter.job_starts_at, hour=19)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter.job_starts_at, hour=19, minute=30)

    def test_babysitter_ends_no_later_than_4AM(self):
        self.assertRaises(EndsTooLate, self.babysitter.job_ends_at, hour=5)
        self.assertRaises(EndsTooLate, self.babysitter.job_ends_at, hour=4, minute=30)

    def test_babysitter_ends_no_later_than_4AM_but_accepts_5PM_to_midnight(self):
        self.babysitter.job_ends_at(17)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(17))
        self.babysitter.job_ends_at(23)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(23))
        self.babysitter.job_ends_at(17, 30)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(17, 30))

    def test_babysitter_sets_end_time_when_it_is_not_later_than_4AM(self):
        self.babysitter.job_ends_at(4)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(4))
        self.babysitter.job_ends_at(3, 30)
        self.assertEqual(self.babysitter.end_time, BabysitterTime(3, 30))

    def test_babysitter_end_time_must_be_after_start_time(self):
        self.babysitter.job_starts_at(20)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter.job_ends_at, 18)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter.job_ends_at, 18, 30)
        self.babysitter.job_starts_at(20, 30)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter.job_ends_at, 18)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter.job_ends_at, 18, 30)

    def test_babysitter_sets_bedtime_for_any_time(self):
        self.babysitter.bedtime_is(7)
        self.assertEqual(self.babysitter.bedtime, BabysitterTime(7))
        self.babysitter.bedtime_is(7, 30)
        self.assertEqual(self.babysitter.bedtime, BabysitterTime(7, 30))

    def test__is_invalid_time(self):
        self.assertTrue(self.babysitter._is_invalid_time(16))
        self.assertTrue(self.babysitter._is_invalid_time(5))
        self.assertFalse(self.babysitter._is_invalid_time(17))
        self.assertFalse(self.babysitter._is_invalid_time(0))
        self.assertTrue(self.babysitter._is_invalid_time(16, 30))
        self.assertTrue(self.babysitter._is_invalid_time(4, 1))
        self.assertFalse(self.babysitter._is_invalid_time(17, 30))
        self.assertFalse(self.babysitter._is_invalid_time(0, 30))
        self.assertFalse(self.babysitter._is_invalid_time(4))

    def test__is_start_time_after_end_time(self):
        self.babysitter.job_ends_at(20)
        self.assertTrue(self.babysitter._is_start_time_after_end_time(21))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(1))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(18))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(20, 1))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(1, 30))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(18, 30))

        self.babysitter.job_ends_at(20, 30)
        self.assertTrue(self.babysitter._is_start_time_after_end_time(21))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(1))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(18))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(20, 31))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(1, 30))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(18, 30))

        self.babysitter.job_ends_at(2)
        self.assertTrue(self.babysitter._is_start_time_after_end_time(3))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(20))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(1))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(2, 1))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(20, 30))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(1, 30))

        self.babysitter.job_ends_at(2, 30)
        self.assertTrue(self.babysitter._is_start_time_after_end_time(3))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(20))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(1))
        self.assertTrue(self.babysitter._is_start_time_after_end_time(2, 31))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(20, 30))
        self.assertFalse(self.babysitter._is_start_time_after_end_time(1, 30))

    def test__is_end_time_before_start_time(self):
        self.babysitter.job_starts_at(20)
        self.assertFalse(self.babysitter._is_end_time_before_start_time(21))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(1))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(18))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(20, 1))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(1, 30))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(19, 59))

        self.babysitter.job_starts_at(20, 30)
        self.assertFalse(self.babysitter._is_end_time_before_start_time(21))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(1))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(18))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(20, 31))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(1, 30))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(20, 29))

        self.babysitter.job_starts_at(2)
        self.assertFalse(self.babysitter._is_end_time_before_start_time(3))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(20))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(1))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(2, 1))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(20, 30))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(1, 59))

        self.babysitter.job_starts_at(2, 30)
        self.assertFalse(self.babysitter._is_end_time_before_start_time(3))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(20))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(1))
        self.assertFalse(self.babysitter._is_end_time_before_start_time(2, 31))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(20, 30))
        self.assertTrue(self.babysitter._is_end_time_before_start_time(2, 29))

    def test__is_valid_start_time(self):
        self.assertRaises(StartsTooEarly, self.babysitter._is_valid_start_time, 16)
        self.babysitter.job_ends_at(18)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter._is_valid_start_time, 19)
        self.assertTrue(self.babysitter._is_valid_start_time(17))
        self.assertRaises(StartsTooEarly, self.babysitter._is_valid_start_time, 16, 59)
        self.babysitter.job_ends_at(18, 30)
        self.assertRaises(StartTimeAfterEndTime, self.babysitter._is_valid_start_time, 18, 31)
        self.assertTrue(self.babysitter._is_valid_start_time(18, 29))

    def test__is_valid_end_time(self):
        self.assertRaises(EndsTooLate, self.babysitter._is_valid_end_time, 5)
        self.babysitter.job_starts_at(20)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter._is_valid_end_time, 18)
        self.assertTrue(self.babysitter._is_valid_end_time(21))
        self.assertRaises(EndsTooLate, self.babysitter._is_valid_end_time, 4, 1)
        self.babysitter.job_starts_at(20, 30)
        self.assertRaises(EndTimeBeforeStartTime, self.babysitter._is_valid_end_time, 20, 29)
        self.assertTrue(self.babysitter._is_valid_end_time(20, 31))

    def test__get_full_hours_at_12_hourly_rate_with_times_in_order_and_bedtime_before_midnight(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.bedtime_is(20)
        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 3)

        self.babysitter.job_starts_at(17)
        self.babysitter.bedtime_is(20, 30)
        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 3)

    def test__get_full_hours_at_12_hourly_rate_with_times_in_order_and_bedtime_after_midnight(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.bedtime_is(1)
        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 7)

        self.babysitter.job_starts_at(17, 30)
        self.babysitter.bedtime_is(1)
        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 6)

    def test__get_full_hours_at_12_hourly_rate_with_bedtime_before_start_time(self):
        self.babysitter.job_starts_at(19)
        self.babysitter.bedtime_is(17)
        self.babysitter.job_ends_at(1)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 0)

        self.babysitter.job_starts_at(17)
        self.babysitter.bedtime_is(13)
        self.babysitter.job_ends_at(1)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 7)

    def test__get_full_hours_at_12_hourly_rate_with_no_bedtime(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.job_ends_at(1)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 7)

    def test__get_full_hours_at_12_hourly_rate_with_endtime_before_midnight(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.job_ends_at(19)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 2)

        self.babysitter.bedtime_is(18)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 1)

        self.babysitter.bedtime_is(20)
        self.assertEqual(self.babysitter._get_full_hours_at_12_hourly_rate(), 2)

    def test__get_full_hours_at_8_hourly_rate_when_no_bedtime(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.job_ends_at(1)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 0)

    def test__get_full_hours_at_8_hourly_rate_when_bedtime_after_end_time(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.job_ends_at(20)
        self.babysitter.bedtime_is(22)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 0)

        self.babysitter.bedtime_is(2)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 0)

        self.babysitter.job_ends_at(1)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 0)

    def test__get_full_hours_at_8_hourly_rate_when_bedtime_after_midnight(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.job_ends_at(3)
        self.babysitter.bedtime_is(1)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 0)

    def test__get_full_hours_at_8_hourly_rate_for_other_cases(self):
        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(23)
        self.babysitter.bedtime_is(19)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 4)

        self.babysitter.bedtime_is(17)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 5)

        self.babysitter.job_ends_at(1)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 6)

        self.babysitter.bedtime_is(19)
        self.assertEqual(self.babysitter._get_full_hours_at_8_hourly_rate(), 5)

    def test__get_full_hours_at_16_hourly_rate(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.job_ends_at(23)
        self.assertEqual(self.babysitter._get_full_hours_at_16_hourly_rate(), 0)

        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter._get_full_hours_at_16_hourly_rate(), 2)

    def test__calculate_pay_with_bedtime(self):
        self.babysitter.bedtime_is(17)
        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(22)
        self.assertEqual(self.babysitter.calculate_pay(), 32)

        self.babysitter.job_starts_at(18)
        self.babysitter.bedtime_is(20)
        self.babysitter.job_ends_at(22)
        self.assertEqual(self.babysitter.calculate_pay(), 40)

        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(19)
        self.babysitter.bedtime_is(20)
        self.assertEqual(self.babysitter.calculate_pay(), 12)

        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(19)
        self.babysitter.bedtime_is(2)
        self.assertEqual(self.babysitter.calculate_pay(), 12)

        self.babysitter.bedtime_is(17)
        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter.calculate_pay(), 80)

        self.babysitter.job_starts_at(18)
        self.babysitter.bedtime_is(20)
        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter.calculate_pay(), 88)

        self.babysitter.job_starts_at(18)
        self.babysitter.bedtime_is(1)
        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter.calculate_pay(), 104)

        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(2)
        self.babysitter.bedtime_is(3)
        self.assertEqual(self.babysitter.calculate_pay(), 104)

    def test__calculate_pay_without_bedtime(self):
        self.babysitter.job_starts_at(17)
        self.babysitter.job_ends_at(22)
        self.assertEqual(self.babysitter.calculate_pay(), 60)

        self.babysitter.job_ends_at(2)
        self.assertEqual(self.babysitter.calculate_pay(), 116)


    def test__calculate_pay_with_bedtime_with_fractional_hours(self):
        self.babysitter.bedtime_is(17)
        self.babysitter.job_starts_at(18, 10)
        self.babysitter.job_ends_at(22, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 32)

        self.babysitter.job_starts_at(18)
        self.babysitter.bedtime_is(20, 10)
        self.babysitter.job_ends_at(22, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 40)

        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(19, 10)
        self.babysitter.bedtime_is(20, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 12)

        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(19, 10)
        self.babysitter.bedtime_is(2, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 12)

        self.babysitter.bedtime_is(17)
        self.babysitter.job_starts_at(18, 10)
        self.babysitter.job_ends_at(2, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 72)

        self.babysitter.job_starts_at(18)
        self.babysitter.bedtime_is(20, 10)
        self.babysitter.job_ends_at(2, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 80)

        self.babysitter.job_starts_at(18)
        self.babysitter.bedtime_is(1, 10)
        self.babysitter.job_ends_at(2, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 104)

        self.babysitter.job_starts_at(18)
        self.babysitter.job_ends_at(2, 10)
        self.babysitter.bedtime_is(3, 20)
        self.assertEqual(self.babysitter.calculate_pay(), 104)


if __name__ == '__main__':
    unittest.main()