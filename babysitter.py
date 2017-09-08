from babysitter_time import *


class Babysitter:
    earliest_start_allowed = BabysitterTime(BabysitterTime.earliest_start_allowed)
    latest_end_allowed = BabysitterTime(BabysitterTime.latest_end_allowed)
    midnight = BabysitterTime(0)

    def _get_full_hours_at_12_hourly_rate(self):
        try:
            if self.bedtime < self.start_time:
                return 0
            else:
                time = min(self.bedtime, self.end_time, self.midnight)
                return time.full_hours_since(self.start_time)
        except AttributeError:
            time = min(self.end_time, self.midnight)
            return time.full_hours_since(self.start_time)

    def _get_full_hours_at_8_hourly_rate(self):
        try:
            if self.bedtime:
                return 0
        except AttributeError:
            return 0

    def job_starts_at(self, hour, minute=None):
        if self._is_valid_start_time(hour, minute):
            self.start_time = BabysitterTime(hour, minute)

    def _is_valid_start_time(self, hour, minute=None):
        if self._is_invalid_time(hour, minute):
            raise StartsTooEarly()
        elif self._is_start_time_after_end_time(hour, minute):
            raise StartTimeAfterEndTime()
        else:
            return True

    def job_ends_at(self, hour, minute=None):
        if self._is_valid_end_time(hour, minute):
            self.end_time = BabysitterTime(hour, minute)

    def _is_valid_end_time(self, hour, minute=None):
        if self._is_invalid_time(hour, minute):
            raise EndsTooLate()
        elif self._is_end_time_before_start_time(hour, minute):
            raise EndTimeBeforeStartTime()
        else:
            return True

    def bedtime_is(self, hour, minute=None):
            self.bedtime = BabysitterTime(hour, minute)

    def _is_start_time_after_end_time(self, hour, minute=None):
        try:
            return BabysitterTime(hour, minute) > self.end_time
        except AttributeError:
            return False

    def _is_end_time_before_start_time(self, hour, minute=None):
        try:
            return BabysitterTime(hour, minute) < self.start_time
        except AttributeError:
            return False

    def _is_invalid_time(self, hour, minute=None):
        return BabysitterTime(hour, minute) < self.earliest_start_allowed \
               or BabysitterTime(hour, minute) > self.latest_end_allowed


class StartsTooEarly(Exception):
    pass


class EndsTooLate(Exception):
    pass


class StartTimeAfterEndTime(Exception):
    pass


class EndTimeBeforeStartTime(Exception):
    pass
