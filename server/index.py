import socket

from signal import signal, SIGPIPE, SIG_DFL   
signal(SIGPIPE,SIG_DFL) 

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for connections...")
connection, client_address = server_socket.accept()

while True:
    try:
        msg = connection.recv(1024)
        if len(msg.decode()) > 0:
            print("recieve: " + msg.decode())
            connection.send(f"[Server receive _ {msg.decode()}]".encode())
    except:
        connection.close()