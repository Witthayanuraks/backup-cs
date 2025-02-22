import argparse
import subprocess
from typing import List, Dict
import scapy.all as scapy


def get_open_ports(ip: str) -> List[int]:
    ports = []
    for port in range(int(args.port_range.split('-')[0]), int(args.port_range.split('-')[1]) + 1):
        try:
            scapy.sr1(scapy.IP(dst=ip)/scapy.UDP(dport=port), timeout=1, verbose=False)
            ports.append(port)
        except scapy.error.TimeoutError:
            pass
    return ports
def get_arguments() -> argparse.Namespace:
    # parser = argparse.ArgumentParser(description='Scan network for open UDP ports')
    # parser.add_argument('-i', '--interface', type=str, required=True, help='Network interface to scan')
    # parser.add_argument('-p', '--port-range', type=str, default='1-65535', help='Port range to scan (default: 1-65535)')
    # parser.add_argument('-o', '--output', type=str, default='open_ports.txt', help='Output file (default: open_ports.txt)')
    # return parser.parse_args()
    """Parses command-line arguments and returns target IP or IP range."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Specify target IP or IP range")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify target IP or IP range.")
    return options

# 1 ( IPv4)
def scan(ip: str) -> List[Dict[str, str]]:
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet,
                              timeout=1, verbose=False)[0]
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list
# 2 (IPv6)
def scan_network(target: str, ports: List[int]) -> Dict[int, bool]:
    results = {}
    for port in ports:
        response = scapy.sr1(scapy.IP(dst=target) / scapy.UDP(dport=port), timeout=1, verbose=0)
        if response:
            results[port] = True
        else:
            results[port] = False
    return results
    
def print_result(scan_list: List[Dict[str, str]]) -> None:
    print("IP\t\t\tMAC\n----------------------------------------")
    for client in scan_list:
        print(f"{client['ip']}\t\t{client['mac']}")

#3 
def scan_auto( targets: List[Dict[str, str]]):
    port_range = range(1, 65536)
    results = {}
    for target in targets:
        results[target['ip']] = scan_network(target['ip'], port_range)
    return results

if __name__ == '__main__':
    options = get_arguments()
    result_list = scan(options.target)
    print_result(result_list)