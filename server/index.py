import socket
from _thread import start_new_thread
import sys
import json
from receive_handle import receiveHandle
from encode import encode
from decode import decode

server = "0.0.0.0"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(f"Error binding the socket: {e}")
    sys.exit(1)

s.listen(2)

# Get the local hostname
hostname = socket.gethostname()
# Get the local IP address
local_ip = socket.gethostbyname(hostname)
print("Waiting for a connection, Server Started")
print(f"Server started at: {local_ip}:{8080}")

player = {"0": {"id": 0, "connected": False}, "1": {"id": 1, "connected": False}}
running = True  # Flag to control the server loop

# Function to handle client connections
def threaded_client(conn: socket, addr, player_id: int):
    try:
        conn.send(encode({"action": 3, "data": {"currPlayer": player_id}}))
        while True:
            try:
                # Receive data from the client
                data = conn.recv(2048)
                if data:
                    decodeData = decode(data)
                    receiveHandle(conn, decodeData, player_id)
                else:
                    # No data received, client closed the connection
                    break
            except json.JSONDecodeError as e:
                print("JSON decoding error:", e)
            except socket.error as e:
                print("Socket error:", e)
                break
    finally:
        print(f"Player {player_id} disconnected")
        for key, value in player.items():
            if value["id"] == player_id:
                value["connected"] = False
                break
        conn.close()

# Main server loop
while running:
    try:
        if not player["0"]["connected"] or not player["1"]["connected"]:
            conn, addr = s.accept()
            print("New connection:", addr)
            # Assign the first available slot for the player
            for key, value in player.items():
                if not value["connected"]:
                    start_new_thread(threaded_client, (conn, addr, value["id"]))
                    value["connected"] = True
                    break
            print("Player: ", player)
    except Exception as e:
        print(f"Server error: {e}")
        running = False

# Clean up after server loop ends
s.close()
print("Server has been shut down.")
