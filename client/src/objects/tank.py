class Tank:
    def __init__(self, x, y, direction, rotationAngle, speed=50, state=True):
        self.position = {'x': x, 'y': y}
        self.direction = direction
        self.rotationAngle = rotationAngle
        self.speed = speed
        self.state = state

    def move(self, dx, dy):
        self.position['x'] += dx
        self.position['y'] += dy
