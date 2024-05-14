#Source: https://stackoverflow.com/questions/56303279/typeerror-a-bytes-like-object-is-required-not-str-in-python3-http-request
#!/usr/bin/env python

import scapy.all as scapy
from scapy_http import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)


sniff("eth0")