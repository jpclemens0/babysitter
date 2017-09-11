import datetime


# Any time 5 PM or later is interpreted as today.  Any time "earlier" than 5 PM is interpreted as tomorrow.
class BabysitterTime:
    earliest_start_allowed = 17
    latest_end_allowed = 4
    today = datetime.date(1970, 1, 1)
    tomorrow = today + datetime.timedelta(days=1)

    def __init__(self, hour, minute=None):
        if minute is None:
            if hour < self.earliest_start_allowed:
                self.time = datetime.datetime.combine(self.tomorrow, datetime.time(hour))
            else:
                self.time = datetime.datetime.combine(self.today, datetime.time(hour))
        else:
            if hour < self.earliest_start_allowed:
                self.time = datetime.datetime.combine(self.tomorrow, datetime.time(hour, minute))
            else:
                self.time = datetime.datetime.combine(self.today, datetime.time(hour, minute))

    def __lt__(self, other):
        return self.time < other.time

    def __le__(self, other):
        return self.time <= other.time

    def __gt__(self, other):
        return self.time > other.time

    def __ge__(self, other):
        return self.time >= other.time

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    def __sub__(self, other):
        return self.time - other.time

    def full_hours_since(self, other):
        return (self.time - other.time).total_seconds()//3600
