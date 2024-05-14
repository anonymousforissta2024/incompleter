#Source: https://stackoverflow.com/questions/41433908/attributeerror-when-trying-to-use-colorama-not-a-good-title-i-know
from colorama import Fore, Back, Style, init
init()
def colorprint(str1, str2):
    print(Fore.str2 + str1 + Fore.WHITE)
colorprint("words", "GREEN")