#Source: https://stackoverflow.com/questions/30797220/python-3-x-attributeerror-nonetype-object-has-no-attribute-groupdict
import re

fmt = (r"\+((?P<day>\d+)d)?((?P<hrs>\d+)h)?((?P<min>\d+)m)?"
       r"((?P<sec>\d+)s)?((?P<ms>\d+)ms)?$")
p = re.compile(fmt)
match = p.search('Total run time: 9h 34m 9s 901ms realtime, 7h 6m 29s 699ms uptime')
try:
    d = match.groupdict()
except IndexError:
    print("exception here")