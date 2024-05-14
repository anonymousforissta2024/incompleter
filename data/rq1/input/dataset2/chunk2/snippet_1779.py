#Source: https://stackoverflow.com/questions/38441889/get-nameerror-name-ip-is-not-defined-error-message
#!/usr/bin/python

#for python 3 , must install scapy for python3 first by type command "pip3 install scapy-python3"
import scapy.all

frame = scapy.all.Ether(dst="15:16:89:fa:dd:09") / IP(dst="9.16.5.4") / TCP() / "This is my payload"