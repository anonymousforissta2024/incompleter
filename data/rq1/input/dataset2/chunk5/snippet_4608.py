#Source: https://stackoverflow.com/questions/66494598/nameerror-name-update-is-not-defined-ponyorm
from pony.orm import *

customer = update(c.set(CustomerCode = '123') for c in Customers if c.CustomerCode == '456')