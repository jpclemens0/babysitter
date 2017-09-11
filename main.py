from babysitter import *

babysitter1 = Babysitter()
babysitter1.job_starts_at(18, 30)
babysitter1.bedtime_is(20, 15)
babysitter1.job_ends_at(0, 20)
format = '%I:%M %p'
print("The job begins at " + babysitter1.start_time.time.strftime(format) +
      ", ends at " + babysitter1.end_time.time.strftime(format) +
      ", and bedtime is " + babysitter1.bedtime.time.strftime(format) + ".")
print("The pay for this job is $" + str(babysitter1.calculate_pay()) + ".")