import math

class Tank:
    def __init__(self, x, y, speed=0.5, state=True):
        self.position = {'x': x, 'y': y}
        self.speed = speed
        self.state = state

    def move(self, dx, dy):
        self.position['x'] += dx
        self.position['y'] += dy
        
    def get_angle(self, x1, y1, x2, y2):
        angle = math.atan2(y2 - y1, x2 - x1)
        return math.degrees(angle)
