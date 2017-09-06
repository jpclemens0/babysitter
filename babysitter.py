import datetime

class Babysitter:

    def job_starts_at(self, start_time):
        if start_time < datetime.time(17):
            raise StartsTooEarly()
        else:
            self.start_time = start_time

    def job_ends_at(self, end_time):
        if end_time > datetime.time(4) and end_time < datetime.time(17):
            raise EndsTooLate()
        else:
            self.end_time = end_time

    def bedtime_is(self, bedtime):
        if bedtime < self.start_time or bedtime > self.end_time:
            raise InvalidBedtime()
        else:
            self.bedtime = bedtime

class StartsTooEarly(Exception):
    pass

class EndsTooLate(Exception):
    pass

class InvalidBedtime(Exception):
    pass