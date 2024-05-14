#Source: https://stackoverflow.com/questions/55707938/typeerror-when-extracting-pincode-from-resume
import re 

def pincode_fetch(pincode):
    pincode = re.search(r"^[1-9]\d{5}$", pincode)
    return pincode

print(pincode_fetch(datas))