#Source: https://stackoverflow.com/questions/64963543/issues-with-python-decrypt-file-type-error
from StringIO import StringIO
import os
import tkFileDialog

def crypt(t, k):
    old = StringIO(t)
    new = StringIO(t)
    
    for position in xrange(len(t)):
        bias = ord(k[position % len(k)])
        
        old_char = ord(old.read(1))
        new_char = chr(old_char ^ bias)
        
        new.seek(position)
        new.write(new_char)
    
    new.seek(0)
    return new.read()


dirname = tkFileDialog.askdirectory(initialdir="/",  title='Please select a directory')
files = [f for f in os.listdir(dirname) if os.path.join(dirname, f)]
for f in files:
    t = os.path.join(dirname, f)
    tout = os.path.join(dirname, 'decr_%s' % f)
    
    f_in = open(t, 'rb')
    f_out = open(tout, 'wb')
    key = "b8,xaA3rvXb-d&w8P6!9k7dQs.dbkLEw?t!3!`sM(,f!2^6h"
    f_out.write(crypt(f_in.read(), key))
    f_in.close()
    f_out.close()