import datetime

class Babysitter:

    def job_starts_at(self, start_time):
        if start_time < datetime.time(17):
            raise StartsTooEarly()

class StartsTooEarly(Exception):
    pass
