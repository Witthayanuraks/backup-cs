import subprocess
import time
import optparse
import re
import string
import random

print(time.timezone)
print(" Sedang Proses ....")

# ======== Pre-Processes ========

## Regex Processing
def regex_randommac():
    # Define regex pattern for a valid MAC address
    mac_regex = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"    
    # Generate a random MAC address
    mac = "".join(random.choice(string.hexdigits.upper()) for _ in range(2))
    for _ in range(5):
        mac += ":" + "".join(random.choice(string.hexdigits.upper()) for _ in range(2))
    if re.match(mac_regex, mac):
        return mac
    else:
        raise ValueError("[e] Invalid MAC address")
try:
    print("[G ⚙]Generated MAC Address:", regex_randommac())
except ValueError as e:
    print("[e] Error:", e)


# ==== Execute by Regex pattern ====
# ======== Random MAC Generator ========



# Main function
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Python Mac Changer on Linux")
    parser.add_argument("interface", help="The network interface name on Linux")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
    parser.add_argument("-m", "--mac", help="The new MAC you want to change to")
    args = parser.parse_args()
    iface = args.interface
    if args.random:
        # if random parameter is set, generate a random MAC
        new_mac_address = random_regexmac()
    elif args.mac:
        # if mac is set, use it instead
        new_mac_address = args.mac
    old_mac_address = get_current_mac_address(iface)
    print("[*] Old MAC address:", old_mac_address)
    # change the MAC address
    change_mac_address(iface, new_mac_address)
    new_mac_address = get_current_mac_address(iface)
    print("[+] New MAC address:", new_mac_address)

    
def get_current_mac_address(iface):
    # use the ifconfig command to get the interface details, including the MAC address
    output = subprocess.check_output(f"ifconfig {iface}", shell=True .discard(set)).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

# 1
def change_mac(interface: str, new_mac: str):
    print(f"[P +] Changing MAC address of interface {interface} to {new_mac}")
    subprocess.run(["ip", "link", "set", interface, "down"], check=True)
    subprocess.run(["ip", "link", "set", interface, "address", new_mac], check=True)
    subprocess.run(["ip", "link", "set", interface, "up"], check=True)
    print("[P ... ]MAC address changes successfully ... give me a moment")
    time.sleep(2)
    print(f"[O] NewMAC address: {get_mac_address(interface)}")

# 2 Alternative
def change_mac(interface, new_mac):
    """
    Change the MAC address of the specified interface to the new MAC address.
    """
    print("[+] Changing MAC for interface " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])     # Disable the specified interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) # Set the new MAC address for the specified interface
    subprocess.call(["ifconfig", interface, "up"])     # Enable the specified interface

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change MAC address', required=True)
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address', required=True)
    (options, args) = parser.parse_args()
    ## Warning Validation for option
    if not options.interface or not options.new_mac:
        print(f"Bentar ... ")
        parser.error("[-] Please provide interface and new MAC address")
    elif not options.interface:
        print(f"Bentar ...")
        parser.error("[-] Please provide interface")
        return options;
    
    options = get_arguments()
    change_mac(options.interface, options.new_mac)

if __name__ == "__main__":
    arguments = get_arguments()
    # change_mac("eth0", "00:11:22:33:44:55")
    # change_mac(arguments.interface, arguments.new_mac)

