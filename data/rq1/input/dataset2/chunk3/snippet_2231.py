#Source: https://stackoverflow.com/questions/71181635/psychopy-runtime-error-while-logging-a-message-typeerror-not-supported-b
from psychopy import logging
log = logging.LogFile("WS_Dev.log", level = logging.DEBUG, filemode = "w")
logging.log(logging.DEBUG, "in getArguments()")