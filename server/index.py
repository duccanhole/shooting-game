# import socket
# import json

# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE,SIG_DFL)

# # Create a TCP/IP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the address and port
# server_address = ('localhost', 8080)
# server_socket.bind(server_address)

# # Listen for incoming connections
# server_socket.listen(1)

# print("Server is listening for connections...")
# connection, client_address = server_socket.accept()

# while True:
#     print("listen connection: ", client_address)
#     try:
#         msg = connection.recv(1024)
#         connection.send(msg)
#         # data = json.loads(msg.decode())
#         # if len(data) > 0:
#         #     print("recieve: ", data)
#     except:
#         connection.close()
import socket
from _thread import *
import sys

import json

def decode(data: bytes):
    try:
        res = json.loads(data.decode())
        return res if len(res) > 0 else {}
    except:
        return {}


server = "localhost"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(conn):
    while True:
        try:
            data = conn.recv(2048)

            if data:
                print("Received data: ", decode(data))
                conn.sendall(data)
        except:
            break

    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))