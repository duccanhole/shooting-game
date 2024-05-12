# import socket
# import json

# from signal import signal, SIGPIPE, SIG_DFL

# signal(SIGPIPE, SIG_DFL)

# # Create a TCP/IP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the address and port
# server_address = ("localhost", 8080)
# server_socket.bind(server_address)

# # Listen for incoming connections
# server_socket.listen(1)

# print("Server is listening for connections...")
# connection, client_address = server_socket.accept()

# while True:
#     print("listen connection: ", client_address)
#     try:
#         msg = connection.recv(2048)
#         if msg:
#             connection.sendall(msg)
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


def encode(data: dict):
    return json.dumps(data).encode()


server = "localhost"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn: socket):
    try:
        while True:
            try:
                # Send data to the client
                conn.sendall(encode({"msg": "hello from server"}))

                # Receive data from the client
                data = conn.recv(2048)

                # Check if data is received
                if data:
                    print("Received data: ", decode(data))
                    conn.sendall(data)
                    print("Send data to all client")
                else:
                    # No data received, client closed the connection
                    break
            except json.JSONDecodeError as e:
                # Handle JSON decoding errors
                print("JSON decoding error:", e)
            except socket.error as e:
                # Handle socket errors
                print("Socket error:", e)
                break
    finally:
        print("Lost connection")
        conn.close()


player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))
    player += 1
