#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import time
import datetime

d = datetime.datetime.now()
print d
print d.strftime("%y%m%d%H%M%S%f")
print "date str %s" % str(d)
print "date strftime %s" % d.strftime("%y%m%d%H%M%S%f")

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
print "time clock %s" % str(t.clock())
print "time gmtime %s" % str(t.gmtime())
print "time strftime %s" % str(t.strftime("%y%m%d%H%M%S%a"))
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
print "epoch_time = %s" % str(epoch_time)
cf_epoch_time = epoch_time - 1262304000
print "cf_epoch_time = %s" % str(cf_epoch_time)
