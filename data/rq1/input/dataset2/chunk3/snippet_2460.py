#Source: https://stackoverflow.com/questions/40110816/attributeerror-nonetype-object-has-no-attribute-recv
from sys import argv
from src.bot import *
from src.config.config import *

bot = PartyMachine(config).sock()