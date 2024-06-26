#Source: https://stackoverflow.com/questions/72912852/python3-typeerror-a-bytes-like-object-is-required-not-str
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, json, subprocess, psutil

json_key={}

def cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=2)
    json_key['cpu_usage'] = float(cpu_usage)

def cpu_temp():
    cpu_comm = "sensors |grep 'Core 0' |awk '{print $3}'|sed 's/\+//g;s/°C//g'"
    cpu_value = subprocess.check_output(cpu_comm, shell=True)
    json_key['cpu_temp'] = float(cpu_value.rstrip('\n'))

def disk_percent():
    cmd_uptime = "df -h |grep sda1| awk '{print $5}'| sed 's/%//g'"
    hdd_data = subprocess.check_output(cmd_uptime, shell=True)
    json_key['hdd_percent'] = float(hdd_data.rstrip('\n'))

def used_mem():
    mem_cmd = "free -m |egrep 'cache|Mem' |grep -v used|awk '{print $3}'"
    mem_used = psutil.virtual_memory()
    json_key['used_mem'] = mem_used.total >> 20

def percent_mem():
    mem_percent = psutil.virtual_memory().percent
    json_key['percent_mem'] = mem_percent

'''This function is used to retrive values used by td-agent'''
def print_json():
    print(json.dumps(json_key))

if __name__ == "__main__":
    cpu_usage()
    cpu_temp()
    disk_percent()
    used_mem()
    percent_mem()
    print_json()