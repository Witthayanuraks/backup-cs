import socket
import platform
import sys
import urllib.parse
import argparse
import pathlib
import re
from multiprocessing import Process, Queue, freeze_support
import subprocess
import ipaddress
import textwrap

# Fungsi validasi
def validate_email(email_address):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email_address))

def validate_ipv4(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

def validate_ipv6(ip_address):
    try:
        socket.inet_pton(socket.AF_INET6, ip_address)
        return True
    except socket.error:
        return False

def validate_ip(ip_address):
    return validate_ipv4(ip_address) or validate_ipv6(ip_address)

def validate_domain(domain_name):
    try:
        socket.gethostbyname(domain_name)
        return True
    except socket.gaierror:
        return False

def validate_url(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def validate_mac(mac_address):
    mac_regex = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.match(mac_regex, mac_address))

def validate_ip_range(ip_range):
    try:
        start_ip, end_ip = ip_range.split('-')
        return validate_ip(start_ip.strip()) and validate_ip(end_ip.strip())
    except ValueError:
        return False

def validate_domain_range(domain_range):
    try:
        start_domain, end_domain = domain_range.split('-')
        return validate_domain(start_domain.strip()) and validate_domain(end_domain.strip())
    except ValueError:
        return False

def validate_url_range(url_range):
    try:
        start_url, end_url = url_range.split('-')
        return validate_url(start_url.strip()) and validate_url(end_url.strip())
    except ValueError:
        return False

# Fungsi untuk melakukan ping ke sebuah IP
def ping_ip(ip_address):
    # Parameter berbeda untuk Windows dan sistem lain (Linux/Mac)
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_address]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

# Fungsi untuk scan (ping) range IP [] IPV4
def scan_ip_range(ip_range):
    try:
        start_ip, end_ip = ip_range.split('-')
        start_ip = start_ip.strip()
        end_ip = end_ip.strip()
        if not (validate_ipv4(start_ip) and validate_ipv4(end_ip)):
            print("Range IP tidak valid (pastikan format IPv4).")
            return
        start_int = int(ipaddress.IPv4Address(start_ip))
        end_int = int(ipaddress.IPv4Address(end_ip))
        if start_int > end_int:
            print("IP awal harus lebih kecil atau sama dengan IP akhir.")
            return
        for ip_int in range(start_int, end_int + 1):
            ip_str = str(ipaddress.IPv4Address(ip_int))
            reachable = ping_ip(ip_str)
            status = "reachable" if reachable else "not reachable"
            print(f"{ip_str} is {status}.")
    except Exception as e:
        print(f"Error scanning IP range: {e}")

    # Fungsi untuk melakukan ping ke sebuah domain
    def scan_domain_range(domain_range):
        try:
            start_domain, end_domain = domain_range.split('-')
            start_domain = start_domain.strip()
            end_domain = end_domain.strip()
            if not (validate_domain(start_domain) and validate_domain(end_domain)):
                print("Range domain tidak valid.")
                return
            for domain in range(start_domain, end_domain + 1):
                reachable = ping_domain(domain)
                status = "reachable" if reachable else "not reachable"
                print(f"{domain} is {status}.")
        except Exception as e:
            print(f"Error scanning domain range: {e}")

    # Fungsi untuk melakukan ping ke sebuah URL
    def scan_url_range(url_range):
        try:
            start_url, end_url = url_range.split('-')
            start_url = start_url.strip()
            end_url = end_url.strip()
            if not (validate_url(start_url) and validate_url(end_url)):
                print("Range URL tidak valid.")
                return
            for url in range(start_url, end_url + 1):
                reachable = ping_url(url)
                status = "reachable" if reachable else "not reachable"
                print(f"{url} is {status}.")
        except Exception as e:
            print(f"Error scanning URL range: {e}")
    

# Fungsi utama dengan menu interaktif
def main():
    while True:
        print("\n=== Menu Validasi & Scan ===")
        print("1. Validasi IP address (IPv4/IPv6)")
        print("2. Validasi Email address")
        print("3. Validasi Domain")
        print("4. Validasi URL")
        print("5. Validasi MAC address")
        print("6. Validasi IP range (format: start_ip-end_ip)")
        print("7. Validasi Domain range (format: start_domain-end_domain)")
        print("8. Validasi URL range (format: start_url-end_url)")
        print("9. Ping sebuah IP address")
        print("10. Scan IP range (Ping IPv4)")
        print("11. Keluar")

        choice = input("Milih yang mana? ").strip()

        if choice == "1":
            ip = input("Masukkan IP address untuk validasi: ").strip()
            if validate_ip(ip):
                print(f"{ip} adalah IP address yang valid.")
            else:
                print(f"{ip} TIDAK valid sebagai IP address.")
        elif choice == "2":
            email = input("Masukkan email address untuk validasi: ").strip()
            if validate_email(email):
                print(f"{email} adalah email address yang valid.")
            else:
                print(f"{email} TIDAK valid sebagai email address.")
        elif choice == "3":
            domain = input("Masukkan domain untuk validasi: ").strip()
            if validate_domain(domain):
                print(f"{domain} adalah domain yang valid.")
            else:
                print(f"{domain} TIDAK valid sebagai domain.")
        elif choice == "4":
            url = input("Masukkan URL untuk validasi: ").strip()
            if validate_url(url):
                print(f"{url} adalah URL yang valid.")
            else:
                print(f"{url} TIDAK valid sebagai URL.")
        elif choice == "5":
            mac = input("Masukkan MAC address untuk validasi: ").strip()
            if validate_mac(mac):
                print(f"{mac} adalah MAC address yang valid.")
            else:
                print(f"{mac} TIDAK valid sebagai MAC address.")
        elif choice == "6":
            ip_range = input("Masukkan IP range (format: start_ip-end_ip): ").strip()
            if validate_ip_range(ip_range):
                print(f"{ip_range} memiliki format IP range yang valid.")
            else:
                print(f"{ip_range} TIDAK valid sebagai format IP range.")
        elif choice == "7":
            domain_range = input("Masukkan Domain range (format: start_domain-end_domain): ").strip()
            if validate_domain_range(domain_range):
                print(f"{domain_range} adalah Domain range yang valid.")
            else:
                print(f"{domain_range} TIDAK valid sebagai Domain range.")
        elif choice == "8":
            url_range = input("Masukkan URL range (format: start_url-end_url): ").strip()
            if validate_url_range(url_range):
                print(f"{url_range} adalah URL range yang valid.")
            else:
                print(f"{url_range} TIDAK valid sebagai URL range.")
        elif choice == "9":
            ip = input("Masukkan IP address untuk di-ping: ").strip()
            if validate_ip(ip):
                if ping_ip(ip):
                    print(f"{ip} reachable (dapat dijangkau).")
                else:
                    print(f"{ip} tidak reachable (tidak dapat dijangkau).")
            else:
                print(f"{ip} TIDAK valid sebagai IP address.")
        elif choice == "10":
            ip_range = input("Masukkan IP range untuk scan (format: start_ip-end_ip): ").strip()
            scan_ip_range(ip_range)
        elif choice == "11":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Aku Pergi ...")

if __name__ == "__main__":
    main()
