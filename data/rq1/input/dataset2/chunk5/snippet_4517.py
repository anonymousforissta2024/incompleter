#Source: https://stackoverflow.com/questions/67486095/nameerror-name-status-code-is-not-defined-while-parsing-access-log
import argparse
import json
import re
from collections import defaultdict

parser = argparse.ArgumentParser(description='log parser')
parser.add_argument('-f', dest='logfile', action='store', default='access.log')
args = parser.parse_args()

regul_ip = (r"^(?P<ips>.*?)")
regul_statuscode = (r"\s(?P<status_code>400)\s")


dict_ip = defaultdict(lambda: {"400": 0})

with open(args.logfile) as file:
     for index, line in enumerate(file.readlines()):
        try:
              ip = re.search(regul_ip, line).group()
              status_code = re.search(regul_statuscode, line).groups()[0]
        except AttributeError:
             pass
        dict_ip[ip][status_code] += 1

print(json.dumps(dict_ip, indent=4))
with open("final_log.json", "w") as jsonfile:
    json.dump(dict_ip, jsonfile, indent=5)