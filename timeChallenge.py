# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone _name when displaying the chosen time.
import time

import pytz
import datetime

for x in pytz.all_timezones:
    print(x)

while True:
    choice = input("Please write down a time zone to get info or press `0` to quit : ")
    if choice == '0':
        break
    tz_to_display = pytz.timezone(choice)
    world_time = datetime.datetime.now(tz=tz_to_display)
    print("The time in {} is {} {}".format(choice, world_time.strftime("%A %x %X %z"), world_time.tzname()))
    print("The localtime is {}".format(datetime.datetime.now().strftime("%A %x %X")))
    print("The utctime is {}".format(datetime.datetime.utcnow().strftime("%A %x %X")))
