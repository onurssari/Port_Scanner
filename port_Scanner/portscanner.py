# SuperFastPython.com
# scan a range of port numbers on host one by one
from logging import exception
from socket import AF_INET, gethostbyname
from socket import SOCK_STREAM
from socket import socket
from termcolor import cprint
import pyfiglet
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

    # scan each port number
    try:
        for port in ports:
            if test_port_number(host, port):
                print_green(f'> {host}:{port} open')
    except:
        print_red("Error")
 
def main(argv):
    # define host and port numbers to scan
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print_yellow(ascii_banner)
    HOST="localhost"
    PORT=65536
    try:
        opts, args = getopt.getopt(argv, "ip:p:",["ipaddress", "port"])
    except:
        print("Error")
    for opt, arg in opts:
        if opt in ['-ip', '--ipaddress']:
            HOST = arg
        elif opt in ['-p', '--port']:
            PORT = int(arg)
        else:
            print_red('Wrong options try again')
            
        currentport=range(PORT)
        port_scan(HOST,currentport)
   
   

if __name__ == "__main__":
    print_red=lambda x: cprint(x,'red')
    print_blue=lambda x:cprint(x,'blue')
    print_green=lambda x:cprint(x,'green')
    print_yellow=lambda x:cprint(x,'yellow')
    
    main(sys.argv[1:])