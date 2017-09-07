import datetime

class Babysitter:
    earliest_start_allowed = datetime.time(17)
    latest_end_allowed = datetime.time(4)

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
            if start_time > self.earliest_start_allowed:
                if self.end_time > self.earliest_start_allowed:
                    return start_time > self.end_time
                else:
                    return False
            else:
                if self.end_time > self.earliest_start_allowed:
                    return True
                else:
                    return start_time > self.end_time
        except AttributeError:
            return False

    def _is_end_time_before_start_time(self, end_time):
        try:
            if end_time > self.earliest_start_allowed:
                if self.start_time > self.earliest_start_allowed:
                    return end_time < self.start_time
                else:
                    return True
            else:
                if self.start_time > self.earliest_start_allowed:
                    return False
                else:
                    return end_time < self.start_time
        except AttributeError:
            return False

    def _is_invalid_time(self, time):
        return time < self.earliest_start_allowed and time > self.latest_end_allowed

class StartsTooEarly(Exception):
    pass

class EndsTooLate(Exception):
    pass

class StartTimeAfterEndTime(Exception):
    pass

class EndTimeBeforeStartTime(Exception):
    pass
