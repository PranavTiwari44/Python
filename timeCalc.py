import time
from time import perf_counter as my_timer # can use time, monotonic and process_time, check notes to understand more!
import random

# print(time.gmtime(0))
#
# print(time.localtime())
#
# print(time.time())

# time_here = time.localtime()
# print(time_here)
#
# print("Year: ", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[2], time_here.tm_mday)

input("please enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("please enter to stop")

end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("started at " + time.strftime("%X", time.localtime(end_time)))

print("your reaction time was {} seconds".format(end_time - start_time))