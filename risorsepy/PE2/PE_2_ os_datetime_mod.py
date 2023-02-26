#--------------------- OS MODULE ----------------------#

# uname() function
# returns an object that contains information about the current operating system. The object has the following attributes:

# systemname (stores the name of the operating system)
# nodename (stores the machine name on the network)
# release (stores the operating system release)
# version (stores the operating system version)
# machine (stores the hardware identifier, e.g. x86_64.)


# name attribute 
# available in the os module allows you to distinguish the operating system. It returns one of the following three values:

# posix (you'll get this name if you use Unix)
# nt (you'll get this name if you use Windows)
# java (you'll get this name if your code is written in something like Jython)



##### DIRECTORIES ######
# mkdir() function 
# creates a directory in the path passed as its argument. The path can be either relative or absolute

# makedirs() function, which allows you to recursively create all directories in a path


# listdir() function 
# is a list containing the names of the files and directories that are in the path passed as its argument
#It's important to remember that the listdir function omits the entries '.' and '..', which are displayed, for example, when using the ls -a command on Unix systems. 
# If the path isn't passed, the result will be returned for the current working directory


# chdir() function
# change working directory

# getcwd() function
# find out what the current working directory is
import os
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())

# rmdir() function
# remove a directory

# removedirs() function
# remove a directory and its subdirectories


# SHELL, TERMINAL, CMD

# system() function
# executes a command passed to it as a string
import os
returned_value = os.system("mkdir hello")
# on Windows returns the value returned by the shell after running the command given
# on Unix it returns the exit status of the process



#-------------------DATETIME-------------------#

# provides classes for working with date and time

# event logging, tracking changes in the database, data validation, storing important information

# date class
from datetime import date
today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
my_date = date(2019, 11, 4)



# datetime objects
datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)
# microsecond	The microsecond parameter must be greater than or equal to 0 and less than 1000000.
# tzinfo	The tzinfo parameter must be a tzinfo subclass object or None (default).
# fold	The fold parameter must be 0 or 1 (default 0).



# current date and time
from datetime import datetime
print("today:", datetime.today())       # current local date and time with the tzinfo attribute set to None
print("now:", datetime.now())           # current local date and time the same as the today method, unless
                                        # we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass
print("utcnow:", datetime.utcnow())     # returns the current UTC date and time with the tzinfo attribute set to None 


# timestamp
# expresses the number of seconds since January 1, 1970, 00:00:00 (UTC)
from datetime import date
import time
timestamp = time.time()
print("Timestamp:", timestamp)
d = date.fromtimestamp(timestamp)
print("Date:", d)
# the result of the time function depends on the platform, because in Unix and Windows systems, leap seconds aren't counted

# Getting a timestamp
from datetime import datetime
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
    


# fromisoformat method
# takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard
# available in Python since version 3.7


# replace() method
# replace the year, month, or day with a different value
from datetime import date

d = date(1991, 2, 5)
d = d.replace(year=1992, month=1, day=16)
# returns a changed date object


# weekday method
# return a 0 to 6 value (Mon to Sun), who represents the current weekday 
from datetime import date
d = date(2019, 11, 4)

# isoweekday method
# return a 1 to 7 value (Mon to Sun), who represents the current weekday 


# time(hour, minute, second, microsecond, tzinfo, fold) class
 
# The time class constructor accepts the following optional parameters:

# Parameter	Restrictions
# hour	        The hour parameter must be greater than or equal to 0 and less than 23.
# minute	    The minute parameter must be greater than or equal to 0 and less than 59.
# second	    The second parameter must be greater than or equal to 0 and less than 59.
# microsecond	The microsecond parameter must be greater than or equal to 0 and less than 1000000.
# tzinfo	    The tzinfo parameter must be a tzinfo subclass object or None (default).
# fold	        The fold parameter must be 0 or 1 (default 0).

from datetime import time
t = time(14, 53, 20, 1)



#---------------------------TIME MODULE---------------------------#

# sleep() function
# suspends program execution for the given number of seconds
import time
print("I'm very tired. I have to take a nap. See you later.")
time.sleep(seconds)
print("I slept well! I feel great!")



# ctime() function
# converts the time in seconds since January 1, 1970 (Unix epoch) to a string
import time

timestamp = 1572879180
print(time.ctime(timestamp))
# without specifying the time in seconds the current time will be returned:
import time
print(time.ctime())



# struct_time class
time.struct_time:
    tm_year   # Specifies the year.
    tm_mon    # Specifies the month (value from 1 to 12)
    tm_mday   # Specifies the day of the month (value from 1 to 31)
    tm_hour   # Specifies the hour (value from 0 to 23)
    tm_min    # Specifies the minute (value from 0 to 59)
    tm_sec    # Specifies the second (value from 0 to 61 )
    tm_wday    # Specifies the weekday (value from 0 to 6)
    tm_yday   # Specifies the year day (value from 1 to 366)
    tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # Specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # Specifies the offset east of UTC (value in seconds)
# The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.
# The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes


# gmtime, localtime methods
import time
timestamp = 1572879180
print(time.gmtime(timestamp))       # returns the struct_time object in UTC
print(time.localtime(timestamp))    # returns in local time
    


# asctime, mktime
import time
timestamp = 1572879180
st = time.gmtime(timestamp)
print(time.asctime(st))                                     # converts a struct_time object or a tuple to a string
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))     # converts a struct_time object or a tuple that expresses 
                                                            # the local time to the number of seconds since the Unix epoch
    



# FORMATTING DATE AND TIME
# strftime method in datetime module
from datetime import date
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes



# strftime method in time module
import time
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# https://docs.python.org/3/library/time.html#time.strftime



# strptime() method in datetime method
# creates a datetime object from a string representing a date and time
# requires you to specify the format in which you saved the date and time. Let's see it in an example
from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


# strptime() method in time method
# parses a string representing a time to a struct_time object
import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))



# timedelta class in datetime
# perform some calculations on the date and time
# days, seconds, microseconds, milliseconds, minutes, hours, and weeks - default is set to 0
# !!!!! timedelta object only stores days, seconds, and microseconds internally !!!!!!
from datetime import timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

# Example of automatic generation of the class
from datetime import date, datetime
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)
dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)





#------------------------- CALENDAR MODULE --------------------------#

# Day of the week	Int value	Constant
# Monday	        0	        calendar.MONDAY
# Tuesday	        1	        calendar.TUESDAY
# Wednesday     	2	        calendar.WEDNESDAY
# Thursday	        3	        calendar.THURSDAY
# Friday	        4	        calendar.FRIDAY
# Saturday	        5	        calendar.SATURDAY
# Sunday	        6	        calendar.SUNDAY


# calendar function
# print selected year
import calendar
print(calendar.calendar(2020))
#    OR
calendar.prcal(2020)
# default calendar formatting, you can use the following parameters:

# w – date column width (default 2)
# l – number of lines per week (default 1)
# c – number of spaces between month columns (default 6)
# m – number of columns (default 3)



# month function
# print selected month of the year
import calendar
print(calendar.month(2020, 11))
    # OR
calendar.prmonth()
# default formatting using the following parameters:

# w – date column width (default 2)
# l – number of lines per week (default 1)



# setfirstweekday() function
# change default starting weekday from Monday to selected one
import calendar
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)


# weekday() function
# returns the day of the week as an integer value for the given year, month, and day
import calendar
print(calendar.weekday(2020, 12, 24))
    


# weekheader() function
# requires you to specify the width in characters for one day of the week.
# If the width you provide is greater than 3, you'll still get the abbreviated weekday names consisting of three characters
import calendar
print(calendar.weekheader(2))



# LEAP YEARS
import calendar

print(calendar.isleap(2020))            # return bool if year is leap
print(calendar.leapdays(2010, 2021))    # return leap years in the given range. Up to but not including 2021.



# CREATING CALENDARS
calendar.Calendar           # provides methods to prepare calendar data for formatting;
calendar.TextCalendar       # is used to create regular text calendars;
calendar.HTMLCalendar       # is used to create HTML calendars;
calendar.LocalTextCalendar  # is a subclass of the calendar.TextCalendar class. The constructor of this class 
                                # takes the locale parameter, which is used to return the appropriate months and weekday names.
calendar.LocalHTMLCalendar  # is a subclass of the calendar.HTMLCalendar class. The constructor of this class 
                                # takes the locale parameter, which is used to return the appropriate months and weekday names.



# Calendar class
import calendar  
c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():        #iterator for week day numbers
    print(weekday, end=" ")
    

# itermonthdates() method
# requires specifying the year and month
# iter through days (datetime.date object) of complete weeks in the extended month
import calendar  
c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
# The code displays all days in November 2019. Because the first day of November 2019 was a Friday, 
# the following days are also returned to get the complete week: 
# 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday).
# The last day of November 2019 was a Saturday, so in order to keep the complete week, one more day is returned 12/01/2019 (Friday).


# itermonthdays() method
# like itermonthdays but iterate through integers
import calendar  
c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
# itermonthdates2 – returns days in the form of tuples consisting of a day of the month number and a week day number;
# itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers. .
#   This method has been available since Python version 3.7;
# itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, and a day of the week numbers.
#  This method has been available since Python version 3.7.



# monthdays2calendar() method
# takes the year and month, and then returns a list of weeks in a specific month. Each week is a tuple consisting of day numbers and weekday numbers
import calendar  
c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)

