#Source: https://stackoverflow.com/questions/66137185/python-3-attributeerror-module-sys-has-no-attribute-argv
#! python3
# pw.py password locker program

PASSWORDS = {'email': 'F7min18DDuvMJuxESSLHFhTxFtjvB6',
             'blog': 'VmALQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.agrv) < 2:
    print('Usage: python3 pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)