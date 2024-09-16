import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface you want to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    return options
def mac_changer(interface, new_mac):
    print("[+] Changing MAC address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface])
    mac_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_res))
    if mac_res:
        return mac_res.group(0)
    else:
        print("[-] Could not find MAC Address.")

options = get_args()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

mac_changer(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac==options.new_mac:
    print("[+] MAC Address was succefully changed to " + current_mac)
else:
    print("[-] Failed to change MAC Address.")
