#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
# Default.py
import sys
sys.path.append('/NaverNews/Main/Main')
from Main import *
@NaverNews
def DefaultNews():
    print("Shutting Down the Program")
    exit(0)
DefaultNews()