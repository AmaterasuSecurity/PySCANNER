import pyfiglet
import socket
import os
import sys
import subprocess
import threading
import time
from datetime import datetime
from queue import Queue
from metasploit import msfrpc

subprocess.call('clear', shell=True)

ascii_banner = pyfiglet.figlet_format("PySCANNER")
print(ascii_banner)

# Set socket timeout to a higher value to avoid missing open ports
socket.setdefaulttimeout(1.0)

# Declare list to store discovered ports
discovered_ports = []

# Lock thread during print so we get cleaner outputs
print_lock = threading.Lock()

# Notify user
target = input('Target: ')

# Convert target to IP address, if it is a hostname
# This requires that it actually resolves
t_IP = socket.gethostbyname(target)
print(f'Scanning Host for Open Ports: {t_IP}')


# Define port scan function
def portscan(port):
    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Try to connect
    try:
        # Create/open connection
        conx = s.connect((t_IP, port))

        # Don't let thread contention screw up printing
        with print_lock:
            print(f"port {port} is open")
            discovered_ports.append(str(port))

# Create client object
client = msfrpc.MsfRpcClient('your_username', 'your_password')

# Authenticate with the client
client.login()


        # Close connection
        con
