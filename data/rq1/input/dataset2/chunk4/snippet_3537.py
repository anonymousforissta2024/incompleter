#Source: https://stackoverflow.com/questions/68360067/how-wo-fix-typeerror-unsupported-operand-types-for-datetime-time-and-da
import sys
import os
import datetime
import boto3
import pytz
import time


ST = "05:30"

def test():
  WST1 = datetime.datetime.strptime(ST, '%H:%M').time()
  print(WST1)
  print(WST1.tzinfo)
  ST1 = pytz.utc.localize(WST1)
  print(ST1.tzinfo)
  # ST1 = timezone.localize(WST1)
  print(ST1)
  tz1 = pytz.timezone('Europe/London')
  T1 = tz1.localize(WST1)
  T1 = ST1.replace(tzinfo=pytz.utc).astimezone(tz1)
  print(T1)



test()