#Source: https://stackoverflow.com/questions/57213890/python-nmap-typeerror-list-indices-must-be-integers-or-slices-not-str
import nmap
nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan('192.168.0.1', '80', arguments='-O')
print("Portid: " + nm_scanner['scan']['192.168.0.1']['portused']['portid'])