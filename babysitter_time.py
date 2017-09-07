import datetime

class BabysitterTime:
    earliest_start_allowed = 17
    latest_end_allowed = 4

    def __init__(self, hour):
        if hour < self.earliest_start_allowed:
            self.time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days = 1), datetime.time(hour))
        else:
            self.time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour))

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.time == other.time