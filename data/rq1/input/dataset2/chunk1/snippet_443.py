#Source: https://stackoverflow.com/questions/22848621/how-do-i-solve-nameerror-name-threading-is-not-defined-in-python-3-3
#!/usr/bin/python

import Utilities
import os
import sys
import getopt
import time
from queue import Queue
from threading import Thread

_db_lock=threading.Lock()