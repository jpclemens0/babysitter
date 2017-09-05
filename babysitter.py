import datetime

class Babysitter:

    def job_starts_at(self, start_time):
        if start_time < datetime.time(17):
            raise StartsTooEarly()
        else:
            self.start_time = start_time

    def job_ends_at(self, end_time):
        if end_time > datetime.time(4):
            raise EndsTooLate()

class StartsTooEarly(Exception):
    pass

class EndsTooLate(Exception):
    pass