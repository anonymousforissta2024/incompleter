#Source: https://stackoverflow.com/questions/24271752/why-do-i-get-a-nameerror-or-unboundlocalerror-from-using-a-named-exception
exc = None
try:
    raise Exception
except Exception as exc:
    pass
print(exc)