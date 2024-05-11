import socket
import json

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ("localhost", 8080)
client_socket.connect(server_address)

print("connect to localhost:8080")

while True:
    user_input = input("Enter something (type ':q' to quit): ")

    if user_input.lower() == ":q":
        client_socket.close()
        break
    else:
        data = {"data": user_input}
        encode = json.dumps(data).encode()
        client_socket.send(encode)
        print("You emit:", user_input)

    msg = client_socket.recv(1024)
    print("Recieve data from socket " + msg.decode())
