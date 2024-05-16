import socket

from utils.decode import decode
from utils.encode import encode

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.startData = self.connect()
        
    def connect(self): 
        try:
            self.client.connect(("192.168.1.10", 8080))
            return decode(self.client.recv(2048))
        except:
            pass
        
    def send(self, data):
        try:
            self.client.send(encode(data))
            return decode(self.client.recv(2048))
        except socket.error as e:
            # print(e)
            return {}
            
    def getStartData(self):
        return self.startData

            