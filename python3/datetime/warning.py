#!/usr/bin/env python3
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import time
import datetime

d = datetime.datetime.now()
print(("d = %s" % str(d)))
print(("d = %s" % str(type(d))))
print(("d = %s" % str(dir(d))))
print(d)
print((d.strftime("%y%m%d%H%M%S%f")))
print(("date str %s" % str(d)))
print(("date strftime %s" % d.strftime("%y%m%d%H%M%S%f")))

# %a  Weekday as locale’s abbreviated name.   Sun, Mon, ..., Sat (en_US); So, Mo, ..., Sa (de_DE) (1)
# %A  Weekday as locale’s full name.  Sunday, Monday, ..., Saturday (en_US); Sonntag, Montag, ..., Samstag (de_DE) (1)
# %w  Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.   0, 1, ..., 6     
# %d  Day of the month as a zero-padded decimal number.   01, 02, ..., 31  
# %b  Month as locale’s abbreviated name.  Jan, Feb, ..., Dec (en_US); Jan, Feb, ..., Dez (de_DE) (1)
# %B  Month as locale’s full name.    January, February, ..., December (en_US); Januar, Februar, ..., Dezember (de_DE) (1)
# %m  Month as a zero-padded decimal number.  01, 02, ..., 12  
# %y  Year without century as a zero-padded decimal number.   00, 01, ..., 99  
# %Y  Year with century as a decimal number.  1970, 1988, 2001, 2013   
# %H  Hour (24-hour clock) as a zero-padded decimal number.   00, 01, ..., 23  
# %I  Hour (12-hour clock) as a zero-padded decimal number.   01, 02, ..., 12  
# %p  Locale’s equivalent of either AM or PM.  AM, PM (en_US); am, pm (de_DE) (1), (2)
# %M  Minute as a zero-padded decimal number. 00, 01, ..., 59  
# %S  Second as a zero-padded decimal number. 00, 01, ..., 59 (3)
# %f  Microsecond as a decimal number, zero-padded on the left.   000000, 000001, ..., 999999 (4)
# %z  UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).    (empty), +0000, -0400, +1030    (5)
# %Z  Time zone name (empty string if the object is naive).   (empty), UTC, EST, CST   
# %j  Day of the year as a zero-padded decimal number.    001, 002, ..., 366   
# %U  Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.    00, 01, ..., 53 (6)
# %W  Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.    00, 01, ..., 53 (6)
# %c  Locale’s appropriate date and time representation.  Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE) (1)
# %x  Locale’s appropriate date representation.   08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE) (1)
# %X  Locale’s appropriate time representation.   21:30:00 (en_US); 21:30:00 (de_DE) (1)
# %%  A literal '%' character.    %    



# time
t = time
print(("time clock %s" % str(t.clock())))
print(("time gmtime %s" % str(t.gmtime())))
print(("time strftime %s" % str(t.strftime("%y%m%d%H%M%S%a"))))
# %a  Locale’s abbreviated weekday name.   
# %A  Locale’s full weekday name.  
# %b  Locale’s abbreviated month name.     
# %B  Locale’s full month name.    
# %c  Locale’s appropriate date and time representation.   
# %d  Day of the month as a decimal number [01,31].    
# %H  Hour (24-hour clock) as a decimal number [00,23].    
# %I  Hour (12-hour clock) as a decimal number [01,12].    
# %j  Day of the year as a decimal number [001,366].   
# %m  Month as a decimal number [01,12].   
# %M  Minute as a decimal number [00,59].  
# %p  Locale’s equivalent of either AM or PM. (1)
# %S  Second as a decimal number [00,61]. (2)
# %U  Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (3)
# %w  Weekday as a decimal number [0(Sunday),6].   
# %W  Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (3)
# %x  Locale’s appropriate date representation.    
# %X  Locale’s appropriate time representation.    
# %y  Year without century as a decimal number [00,99].    
# %Y  Year with century as a decimal number.   
# %Z  Time zone name (no characters if no time zone exists).   
# %%  A literal '%' character.     

# http://stackoverflow.com/questions/4548684/how-to-get-the-seconds-since-epoch-from-the-time-date-output-of-gmtime-in-py
epoch_time = int(time.time())
print(("epoch_time = %s" % str(epoch_time)))
cf_epoch_time = epoch_time - 1262304000
print(("cf_epoch_time = %s" % str(cf_epoch_time)))

# d = ['__add__', '__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
d = datetime.datetime.now()
# print "d.astimezone = %s" % str(d.astimezone())
# print "d.combine = %s" % str(d.combine())
print(("d.ctime = %s" % str(d.ctime())))
print(("d.date = %s" % str(d.date())))
print(("d.day = %s" % str(d.day)))
print(("d.dst = %s" % str(d.dst())))
# print "d.fromordinal = %s" % str(d.fromordinal())
# print "d.fromtimestamp = %s" % str(d.fromtimestamp())
print(("d.hour = %s" % str(d.hour)))
print(("d.isocalendar = %s" % str(d.isocalendar())))
print(("d.isoformat = %s" % str(d.isoformat())))
print(("d.isoweekday = %s" % str(d.isoweekday())))
print(("d.max = %s" % str(d.max)))
print(("d.microsecond = %s" % str(d.microsecond)))
print(("d.min = %s" % str(d.min)))
print(("d.minute = %s" % str(d.minute)))
print(("d.month = %s" % str(d.month)))
print(("d.now = %s" % str(d.now())))
print(("d.replace = %s" % str(d.replace())))
print(("d.resolution = %s" % str(d.resolution)))
print(("d.second = %s" % str(d.second)))
# print "d.strftime = %s" % str(d.strftime())
# print "d.strptime = %s" % str(d.strptime())
print(("d.time = %s" % str(d.time())))
print(("d.timetuple = %s" % str(d.timetuple())))
print(("d.timetz = %s" % str(d.timetz())))
print(("d.today = %s" % str(d.today())))
print(("d.toordinal = %s" % str(d.toordinal())))
print(("d.tzinfo = %s" % str(d.tzinfo)))
print(("d.tzname = %s" % str(d.tzname())))
# print "d.utcfromtimestamp = %s" % str(d.utcfromtimestamp())
print(("d.utcnow = %s" % str(d.utcnow())))
print(("d.utcoffset = %s" % str(d.utcoffset())))
print(("d.utctimetuple = %s" % str(d.utctimetuple())))
print(("d.weekday = %s" % str(d.weekday())))
print(("d.year = %s" % str(d.year)))
d2 = datetime.datetime.now()
d3 = d2 - d
print(("d3 = %s" % str(d3)))

it1 = int(time.time())
print(("it1 = %s" % str(it1)))
dt1 = datetime.datetime.fromtimestamp(it1)
print(("time strftime %s" % str(dt1.strftime("%y%m%d%H%M%S%a"))))
d1 = 60 * 60 * 24
# it1 += d1
it1 -= d1
print(("it1 = %s" % str(it1)))
dt1 = datetime.datetime.fromtimestamp(it1)
print(("time strftime %s" % str(dt1.strftime("%y%m%d%H%M%S%a"))))

#datetime.datetime.fromtimestamp(
#        int("1284101485")
#            ).strftime('%Y-%m-%d %H:%M:%S')

if True:
    # it1 = int(time.time())
    it1 = 1475768342
    d1 = 60 * 60 * 24
    for t1 in range(167):
        dt1 = datetime.datetime.fromtimestamp(it1)
        print(("%s time strftime %s" % (str(t1), str(dt1.strftime("%y%m%d%H%M%S%a")))))
        it1 += d1

it1 = int(time.time())
d1 = 60 * 60 * 24
for i1 in range(166):
    dt1 = datetime.datetime.fromtimestamp(it1)    
    # if dt1.year == 2017:
        # print "%s year" % str(dt1.year)
    # if dt1.month == 3:
        # print "%s month" % str(dt1.month)
    if dt1.year == 2017 and dt1.month == 3 and dt1.day == 21:
        print(("%s %s %s %s day" % (str(i1), str(dt1.year), str(dt1.month), str(dt1.day))))
        print(("%s time strftime %s" % (str(i1), str(dt1.strftime("%y%m%d%H%M%S%a")))))
        break
    it1 += d1
