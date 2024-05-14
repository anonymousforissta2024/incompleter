#Source: https://stackoverflow.com/questions/68237545/python-json-object-typeerror
#!/usr/bin/python3
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import json
import time

router = "192.168.178.1"
web_ip_address = "1.1.1.1"

def ping(web_ip_address):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', '-q', web_ip_address]

    return subprocess.call(command) == 0

response = ping(web_ip_address)
localresponse = ping(router)

data = {
    "router_online": localresponse,
    "ip_address": web_ip_address,
    "timestamp": time.ctime()
}

if response == True:
  print((web_ip_address), 'is reachable!')
else:
  print((web_ip_address), 'is unreachable!') #writes the data only if the internet connection is down
  obj = json.loads(data)

  with open('Downtime_Data.json', 'a') as json_file:
    json.dump(obj, json_file, indent = 2 , sort_keys = True,)