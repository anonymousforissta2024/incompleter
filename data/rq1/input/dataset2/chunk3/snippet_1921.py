#Source: https://stackoverflow.com/questions/51105996/scapy-attributeerror-nonetype-object-has-no-attribute-getlayer
#!/usr/bin/env python3
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def portscan(host,dst_port):
    src_port = RandShort()
    SYNACK = 0x12
    RSTACK = 0x14
    tcp_connect = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),verbose=0,timeout=2)

    if(tcp_connect.getlayer(TCP).flags == SYNACK):
        send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="AR"),verbose=0,timeout=2)
        print (dst_port,"is open")

    elif (tcp_connect.getlayer(TCP).flags == RSTACK):
        print (dst_port,"is closed")

if __name__ == '__main__':
    host = '192.168.0.40'
    port = 80
    portscan(host,port)