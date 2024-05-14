#Source: https://stackoverflow.com/questions/59471398/typeerror-a-bytes-like-object-is-required-not-str-in-python3-6-8
#!/usr/bin/env python
from __future__ import print_function
import json
import sys
import os
import re
import subprocess
import datetime
from glob import glob
import boto3

class VariableCollector:
  def getall(self):
    collected_vars = {}
    for name in dir(self):
      #name = name.decode()
      if name.startswith("get_"):
        debug("VariableCollector - Calling: %s" % (name))
        method = getattr(self, name)
        collected_vars[name] = method()
        collected_vars[name + ":no_quotes"] = collected_vars[name].replace("'","")

        debug("Function: [%s] Value: [%s]" % ( name, collected_vars[name] ))
    return collected_vars