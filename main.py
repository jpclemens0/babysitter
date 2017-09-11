from babysitter import *

babysitter1 = Babysitter()
babysitter1.job_starts_at(18, 30)
babysitter1.bedtime_is(20, 15)
babysitter1.job_ends_at(0, 20)
print("The job begins at 6:30 PM, ends at 12:20 AM, and bedtime is 8:15 PM.")
print("The pay for this job is " + str(babysitter1.calculate_pay()) + " dollars.")