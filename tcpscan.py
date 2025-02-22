import socket
import optparse
import threading

print(f"Starting ................")
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()

# 1
def main():
    parser = optparse.OptionParser("usage%prog -H <target host> -p <target port>")
    parser.add_option("-H", dest="tgt_host", type="string", help="specify target host")
    parser.add_option("-p", dest="tgt_port", type="int", help="specify target port")
    (options, args) = parser.parse_args()
    if not options.tgt_host or not options.tgt_port:
        print(parser.usage)
        exit(0)

    if __name__ == "__main__":
        for port in range(options.tgt_port, options.tgt_port+10):
            t = threading.Thread(target=scan_port, args=(options.tgt_host, port))
            t.start()
#2 
def main():
    parser = optparse.OptionParser(
        "usage%prog -H <specify target host> -p <specify ports separated by ','>")
    parser.add_option("-H", '--host', dest='target_host',
                      type='string', help='specify target host')
    parser.add_option("-p", "--ports", dest='target_ports', type='string',
                      help='specify target ports separated by ","')

    options, args = parser.parse_args()

    if not options.target_host or not options.target_ports:
        print(parser.usage)
        exit()

    host_ip = socket.gethostbyname(options.target_host)
    ports = options.target_ports.split(",")

    for port in ports:
        t = threading.Thread(target=port_scan, args=(host_ip, port))
        t.start()

print(f"Re-Processing ..........")
print(f"Please Wait ................")