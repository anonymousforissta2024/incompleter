#Source: https://stackoverflow.com/questions/49347840/python-3-on-windows-typeerror-an-integer-is-required-got-type-str
#!/usr/bin/env python
import sys, os, socket

def SCAN_TCP_PORT():
    DstIP = input('\nDestination IP Address: ')
    DstPort = input('Port number: ')
    print ('Host %s port %s' % (DstIP, DstPort))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DstIP, DstPort))
    print("%s is listening on TCP port %s" % (DstIP, DstPort))

SCAN_TCP_PORT()