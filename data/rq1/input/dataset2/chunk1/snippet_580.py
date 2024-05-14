#Source: https://stackoverflow.com/questions/23187916/base64-type-err-typeerror-expected-bytes-not-str
#!/usr/bin/python3.2

import time, sys, os
import base64
#####################
tmp = "/home/gh.txt"
ex = "/home/ex.txt"
if (len(sys.argv) < 2):
    print("enter name of the new dict and key")
else:
    global ns
    ns = sys.argv[1]
    global ps
    ps = sys.argv[2]

dss = "{<%s>:%s}" % (ns, ps)
os.system("touch dss0")
fi0 = open(tmp, "a")

fi0.write(dss)
d64i = base64.b64encode(tmp)
fi = open(ex, "a")
fi.write(d64i)
os.system("rm tmp")