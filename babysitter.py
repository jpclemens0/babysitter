import datetime

class Babysitter:

    def job_starts_at(self, start_time):
        if start_time < datetime.time(17):
            raise StartsTooEarly()

class StartsTooEarly(Exception):
    pass
    # def __init__(self, value):
    #     self.value = value
    #
    # def __str__(self):
    #     return repr(self.value)