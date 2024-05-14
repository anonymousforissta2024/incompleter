#Source: https://stackoverflow.com/questions/65410481/filenotfounderror-errno-2-no-such-file-or-directory-bliblibc-a
import scapy.all as scapy
def scan(ip):
    scapy.arping(ip)
scan("192.168.196.0")