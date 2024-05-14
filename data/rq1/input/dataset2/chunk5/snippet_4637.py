#Source: https://stackoverflow.com/questions/57982592/attributeerror-event-object-has-no-attribute-setevent
from event import *
#First Try:
Event().setEvent("error","This is an error")
#Second Try:
a=Event()
a.setEvent("error","This is an error")