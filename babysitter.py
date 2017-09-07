import datetime
from babysitter_time import *

class Babysitter:
    earliest_start_allowed = BabysitterTime(BabysitterTime.earliest_start_allowed)
    latest_end_allowed = BabysitterTime(BabysitterTime.latest_end_allowed)

    def job_starts_at(self, start_time):
        if self._is_invalid_time(start_time):
            raise StartsTooEarly()
        elif self._is_start_time_after_end_time(start_time):
            raise StartTimeAfterEndTime()
        else:
            self.start_time = start_time

    def job_ends_at(self, end_time):
        if self._is_invalid_time(end_time):
            raise EndsTooLate()
        elif self._is_end_time_before_start_time(end_time):
            raise EndTimeBeforeStartTime()
        else:
            self.end_time = end_time

    def bedtime_is(self, bedtime):
            self.bedtime = bedtime

    def _is_start_time_after_end_time(self, start_time):
        try:
            return start_time > self.end_time
        except AttributeError:
            return False

    def _is_end_time_before_start_time(self, end_time):
        try:
            return end_time < self.start_time
        except AttributeError:
            return False

    def _is_invalid_time(self, time):
        return time < self.earliest_start_allowed or time > self.latest_end_allowed

class StartsTooEarly(Exception):
    pass

class EndsTooLate(Exception):
    pass

class StartTimeAfterEndTime(Exception):
    pass

class EndTimeBeforeStartTime(Exception):
    pass
