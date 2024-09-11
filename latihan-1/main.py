import socket
import sys

host = 'www.github.com'
port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

except socket.error as err:
    print(f"Socket failed created with error: {err}")

try:
    port = 80
    host_ip = socket.gethostbyname(host)
except socket.gaierror:
    print(f"Error resolving the host")
    sys.exit()

s.connect((host_ip, port))
print(f"Socket has successful connected to:")
print(f"Host: {host} => Ip Address: {host_ip} => Port: {port}")