import errno
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 8080)
client_socket.connect(server_address)

while True:
    user_input = input("Enter something (type ':q' to quit): ")

    if user_input.lower() == ":q":
        break
    else:
        print("Emit data to server")
        client_socket.send(user_input.encode())
        print("You entered:", user_input)
        
    msg = client_socket.recv(1024)
    print("Recieve data from socket " + msg.decode())

