import datetime

class BabysitterTime:
    earliest_start_allowed = 17
    latest_end_allowed = 4

    def set(self, hour):
        self.time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour))