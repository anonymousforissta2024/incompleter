#Source: https://stackoverflow.com/questions/63044534/subprocess-call-in-python-getting-error-typeerror-expected-str-bytes-or-os-p
import subprocess 
import optparse 

def ChangeMac(interface, new_mac):
    print("mac changed")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser =optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

ChangeMac(optoins.interface, options.new_mac)