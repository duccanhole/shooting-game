import socket
from _thread import *
import sys

import json

from receive_handle import receiveHandle
from encode import encode
from decode import decode


server = "localhost"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

# Get the local hostname
hostname = socket.gethostname()
# Get the local IP address
local_ip = socket.gethostbyname(hostname)
print("Waiting for a connection, Server Started")
print(f"Server start at: {local_ip}:{8080}")


def threaded_client(conn: socket, addr, player: int):
    try:
        conn.send(encode({"action": 3, "data": {"currPlayer": player}}))
        while True:
            try:
                # Receive data from the client
                data = conn.recv(2048)
                # Check if data is received
                if data:
                    decodeData = decode(data)
                    receiveHandle(conn, decodeData, player)
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
    start_new_thread(threaded_client, (conn, addr, player))
    player += 1
