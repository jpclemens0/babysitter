import unittest
import datetime
from babysitter import *

class TestBabysitter(unittest.TestCase):

    def test_babysitter_starts_no_earlier_than_5PM(self):
        babysitter = Babysitter()
        self.assertRaises(StartsTooEarly, babysitter.job_starts_at, start_time = datetime.time(16))


if __name__ == '__main__':
    unittest.main()