# import time
# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\t Daylight Saving Time is is effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is "+ time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
# print("Local time is "+ time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime()))
import datetime
import pytz

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)

print(datetime.datetime.today())
print(datetime.datetime.now(tz=tz_to_display))
print(datetime.datetime.utcnow())

for x in pytz.all_timezones:
    print("{}: {}".format(x, datetime.datetime.now(pytz.timezone(x))))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=":")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            localtime = datetime.datetime.now(tz_to_display)
            print("\t\t{}: {}".format(zone, localtime))
    else:
        print("\t\tError: No Timezone found!")
