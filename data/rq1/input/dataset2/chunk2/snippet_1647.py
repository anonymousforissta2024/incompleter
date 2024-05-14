#Source: https://stackoverflow.com/questions/51443890/scapy-indexing-traceroute-result-with-get-trace-method-returns-typeerror
from scapy.all import *

target = '52.54.2.173'
result, unans = traceroute(target)

print(result.get_trace().keys())