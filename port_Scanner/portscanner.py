# SuperFastPython.com
# scan a range of port numbers on host one by one
from socket import *
from termcolor import cprint
import pyfiglet
import argparse
import sys
import getopt
 
# returns True if a connection can be made, False otherwise
def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        # set a timeout of a few seconds
        sock.settimeout(3)
        # connecting may fail
        try:
            # attempt to connect
            sock.connect((host, port))
            # a successful connection was made
            return True
        except:
            # ignore the failure
            return False
 
# scan port numbers on a host
def port_scan(host, ports):
    print_blue(f'Scanning {host}...')
    print_blue("-"*50)
    tgtIP = gethostbyname(host)
    # scan each port number
    try:
        for port in ports:
            if test_port_number(tgtIP, port):
                print_green(f'> {tgtIP}:{port} open')
    except:
        print_red("Error")
 
def main(argv):
    # define host and port numbers to scan
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print_yellow(ascii_banner)

    parser = argparse.ArgumentParser(description='denemedeneme')
    parser.add_argument('-i', '--ipaddress', help='specify target host')
    parser.add_argument('-p', '--port', type=int, help='specify target port')
    args = parser.parse_args()
    print_blue(args.ipaddress)
    print_blue(args.port)
    HOST = args.ipaddress
    PORT = args.port
    if (HOST == None) | (PORT == None):
            HOST="localhost"
            PORT=65536
    currentport=int(PORT)
    port_scan(HOST,range(currentport))
   
   

if __name__ == "__main__":
    print_red=lambda x: cprint(x,'red')
    print_blue=lambda x:cprint(x,'blue')
    print_green=lambda x:cprint(x,'green')
    print_yellow=lambda x:cprint(x,'yellow')
    
    main(sys.argv[1:])