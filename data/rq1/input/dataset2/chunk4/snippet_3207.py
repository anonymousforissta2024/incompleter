#Source: https://stackoverflow.com/questions/76497050/python-nornir-attributeerror-nonetype-object-has-no-attribute-get
from nornir import InitNornir

from nornir_netmiko.tasks import netmiko_send_command

from nornir_utils.plugins.functions import print_result

NORNIR_CONFIG_FILE = "/home/aruba/config.yaml"

nr = InitNornir(config_file=NORNIR_CONFIG_FILE)

nr = nr.filter(role="access")

def show_ip(task):
    task.run(task=netmiko_send_command, command_string="show ip")

result = nr.run(task=show_ip)

if __name__ == "__main__":
    print_result(result)