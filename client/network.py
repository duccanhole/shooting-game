import socket

from utils.decode import decode
from utils.encode import encode

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.startData =  {
            "data": {
                "currPlayer": -1
            }
        }
        # self.connect()
        
    def connect(self, address: str): 
        try:
            self.client.connect((address, 8080))
            res = decode(self.client.recv(2048))
            self.startData = res
            return res
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

            