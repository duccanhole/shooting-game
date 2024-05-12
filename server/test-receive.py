import socket
import json

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ("localhost", 8080)
client_socket.connect(server_address)

while True:
    msg = client_socket.recv(2048)
    print("Recieve data from socket " + msg.decode())