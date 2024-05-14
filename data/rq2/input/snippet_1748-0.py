import os
if 'C' in query or 'c' in query:
    os.startfile('C:')
elif 'D' in query or 'd' in query:
    os.startfile('D:')
elif 'E' in query or 'e' in query:
    os.startfile('E:')
else:
    print('Wrong Input')