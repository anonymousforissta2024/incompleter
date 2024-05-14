#Source: https://stackoverflow.com/questions/50263360/observing-typeerror-while-trying-to-spawn-to-device
#!/usr/local/lib python3.6
import pexpect
import sys
import re

def dologin(child):
    # Enter User Name
    child.expect ('login:')
    child.sendline ('admin')

    # Enter Password
    child.expect ('Password:')
    child.sendline ('123')
    return

def doprepcommands(child):
    # Enter config prompt
    child.expect ('NOS/27179080475072>')
    child.sendline ('config')

    # Issue command
    child.expect ('NOS/27179080475072/DEBUG/Config>')
    child.sendline ('show vlan')
    child.expect ('NOS/27179080475072/DEBUG/Config>')
    child.sendline ('exit')
    child.expect ('NOS/27179080475072/DEBUG>')
    child.sendline ('exit')
    child.expect ('NOS/27179080475072')
    child.sendline ('exit')
    return

# Spawn the telnet session
child = pexpect.spawn ('telnet 192.168.1.254')

 # Display progress on screen
child.logfile = sys.stdout
dologin(child)
doprepcommands(child)