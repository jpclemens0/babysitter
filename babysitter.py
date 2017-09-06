import datetime

class Babysitter:
    earliest_start_allowed = datetime.time(17)
    latest_end_allowed = datetime.time(4)

    def job_starts_at(self, start_time):
        if self._is_invalid_start_time(start_time):
            raise StartsTooEarly()
        else:
            self.start_time = start_time

    def job_ends_at(self, end_time):
        if end_time > self.latest_end_allowed and end_time < self.earliest_start_allowed:
            raise EndsTooLate()
        else:
            self.end_time = end_time

    def bedtime_is(self, bedtime):
        if bedtime < self.start_time or bedtime > self.end_time:
            raise InvalidBedtime()
        else:
            self.bedtime = bedtime

    def _is_invalid_start_time(self, start_time):
        return start_time < self.earliest_start_allowed and start_time > self.latest_end_allowed

class StartsTooEarly(Exception):
    pass

class EndsTooLate(Exception):
    pass

class InvalidBedtime(Exception):
    pass