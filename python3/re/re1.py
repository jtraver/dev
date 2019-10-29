#!/usr/bin/env python3
#!/usr/bin/python

# http://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string

import re

# regex = re.compile(r'((?P<hours>\d+?)hr)?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)s)?')
regex = re.compile(
    r'((?P<hours>\d+?)\s*h)?((?P<minutes>\d+?)\s*m)?((?P<seconds>\d+?)\s*s)?')


def parse_time(time_str):
    parts = regex.match(time_str)
    if not parts:
        return time_str
    # print parts
    parts = parts.groupdict()
    print parts
    time = 0
    unit = "seconds"
    if parts[unit]:
        time += int(parts[unit])
    unit = "minutes"
    if parts[unit]:
        time += (int(parts[unit]) * 60)
    unit = "hours"
    if parts[unit]:
        time += (int(parts[unit]) * 3600)
    # print time
    if time == 0:
        return time_str
    return time


print parse_time('12hr')
print parse_time('1 hr')
print parse_time('3 minutes')
print parse_time('2')
print parse_time('4 s')
print parse_time('5m')
print parse_time('6s')
print parse_time('7h')
