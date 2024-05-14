#Source: https://stackoverflow.com/questions/52969193/netmiko-attributeerror-nonetype-object-has-no-attribute-recv-ready
    #!/home/ipautowppprod/.pyenv/shims/python

# cisco_auto_back_up_v4

from netmiko import ConnectHandler, redispatch
from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException
import datetime
import sys
import time

now = datetime.datetime.now()
time_now = now.strftime("%Y-%m-%d_%H:%M:%S")

target_info = sys.argv[1].split(',')
ipmon_info = sys.argv[2].split(',')

target_info = [x.strip() for x in target_info]
ipmon_info = [x.strip() for x in ipmon_info]

target_device = {
    'device_type': 'cisco_ios',
    'ip': target_info[0],
    "host": target_info[1],
    'username': target_info[2],
    'password': target_info[3],
    'secret': target_info[4]
}

ipmon = {
    'device_type': 'linux',
    'ip': ipmon_info[0],
    'username': ipmon_info[1],
    'password': ipmon_info[2]
}

try:
    print("Attempting to Connect...")
    # Connect to ipmon
    net_connect = ConnectHandler(**ipmon)
    print(net_connect.find_prompt())

    net_connect.write_channel("ssh {}@{}\n".format(target_device["username"],
                                                   target_device["ip"]))
    time.sleep(1)
    output = net_connect.read_channel()

    print(output)

    if "RSA" in output:
        net_connect.write_channel("yes\n")
        time.sleep(1)
        output = net_connect.read_channel()
        print(output)
    if "user" in output:
        net_connect.write_channel(target_device["username"] + "\n")
        time.sleep(1)
        output = net_connect.read_channel()
    if "password" in output:
        net_connect.write_channel(target_device["password"] + "\n")
        time.sleep(5)
        output = net_connect.read_channel()
    if "password" in output:
        print("Wrong credentials.")
        sys.exit(1)
    elif "refused" in output:
        net_connect.disconnect()
        print("Connection Refused")
    else:
        net_connect.disconnect()

    # Connect to device
    redispatch(net_connect, device_type=target_device['device_type'])
    CMD = net_connect.send_command_timing('show running-config')

    # Converts CMD output to a string
    cmd_output = str(CMD.stdout)

except NetMikoAuthenticationException as autom_err:
    print(autom_err)
    sys.exit(1)

except NetMikoTimeoutException as timeout_err:
    print(timeout_err)
    sys.exit(1)