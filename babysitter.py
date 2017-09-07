import datetime
from babysitter_time import *

class Babysitter:
    earliest_start_allowed = BabysitterTime(BabysitterTime.earliest_start_allowed)
    latest_end_allowed = BabysitterTime(BabysitterTime.latest_end_allowed)

    def job_starts_at(self, start_time):
        if self._is_valid_start_time(start_time):
            self.start_time = BabysitterTime(start_time)

    def _is_valid_start_time(self, start_time):
        if self._is_invalid_time(start_time):
            raise StartsTooEarly()
        elif self._is_start_time_after_end_time(start_time):
            raise StartTimeAfterEndTime()
        else:
            return True

    def job_ends_at(self, end_time):
        if self._is_valid_end_time(end_time):
            self.end_time = BabysitterTime(end_time)

    def _is_valid_end_time(self, end_time):
        if self._is_invalid_time(end_time):
            raise EndsTooLate()
        elif self._is_end_time_before_start_time(end_time):
            raise EndTimeBeforeStartTime()
        else:
            return True

    def bedtime_is(self, bedtime):
            self.bedtime = BabysitterTime(bedtime)

    def _is_start_time_after_end_time(self, start_time):
        try:
            return BabysitterTime(start_time) > self.end_time
        except AttributeError:
            return False

    def _is_end_time_before_start_time(self, end_time):
        try:
            return BabysitterTime(end_time) < self.start_time
        except AttributeError:
            return False

    def _is_invalid_time(self, time):
        return BabysitterTime(time) < self.earliest_start_allowed or BabysitterTime(time) > self.latest_end_allowed

class StartsTooEarly(Exception):
    pass

class EndsTooLate(Exception):
    pass

class StartTimeAfterEndTime(Exception):
    pass

class EndTimeBeforeStartTime(Exception):
    pass
