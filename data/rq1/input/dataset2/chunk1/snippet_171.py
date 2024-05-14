#Source: https://stackoverflow.com/questions/53092781/why-does-my-scan-function-from-the-python-nmap-module-show-str-attribute-erro
import nmap
ns = nmap.PortScanner
ns.scan('My.IP.Add.ress', '1-1024', '-v')
print(ns.scaninfo())