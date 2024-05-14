import re
ipv4 = '^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\\.(\n            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\\.(\n            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\\.(\n            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'

def find(Ip):
    if re.search(ipv4, Ip):
        print('IPv4')
    elif re.search(ipv6, Ip):
        print('IPv6')
    else:
        print('Neither')
if __name__ == '__main__':
    Ip = '192.0.2.126'
    find(Ip)
    Ip = '3001:0da8:75a3:0000:0000:8a2e:0370:7334'
    find(Ip)
    Ip = '36.12.08.20.52'
    find(Ip)