import math
import time
import pygame

CELL_SIZE = 40
class Bullet:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.bulletX = 0
        self.bulletY = 0
        self.isFiring = False
        self.angel = 0
        self.startPos = {'x': 0, 'y': 0}
        self.desPos = [0, 0]
        self.speed = 4
        self.fire_time = None
        
    def addFireAction(self, MAP):
        if self.isFiring: 
            current_time = time.time()
            if (current_time - self.fire_time) > 7:  
                self.isFiring = False
                    
            # Tính toán chỉ số của ô trong bản đồ
            map_x = int(self.bulletX // CELL_SIZE)
            map_y = int(self.bulletY // CELL_SIZE)

            # Kiểm tra va chạm với tường trong bản đồ
            if map_x >= 0 and map_x < len(MAP[0]) and map_y >= 0 and map_y < len(MAP):
                if MAP[map_y][map_x] == 1:
                    if abs(self.speedX) > abs(self.speedY):  # Nếu tốc độ X lớn hơn tốc độ Y, đổi hướng X
                        self.speedX *= -1
                    else:  # Ngược lại, đổi hướng Y
                        self.speedY *= -1
                    # Chuyển viên đạn ra khỏi ô tường
                    self.bulletX += self.speedX
                    self.bulletY += self.speedY
                    return  # Ngừng cập nhật vị trí nếu viên đạn va chạm với tường
            
            self.bulletX += self.speedX
            self.bulletY += self.speedY
            pygame.draw.circle(self.screen, (255, 0, 0), (int(self.bulletX), int(self.bulletY)), 5)
            
    def fire(self, startPos: dict, desPos: tuple):
        if not self.isFiring:
            print('start fire ...')
            self.bulletX = startPos['x']
            self.bulletY = startPos['y']
            self.startPos = startPos
            self.desPos = desPos
            self.isFiring = True
            self.fire_time = time.time()

            dx = self.desPos[0] - self.startPos['x']
            dy = self.desPos[1] - self.startPos['y']
            distance = math.sqrt(dx**2 + dy**2)
            self.speedX = self.speed * (dx / distance)
            self.speedY = self.speed * (dy / distance)
    def getRect(seft): 
        return pygame.Rect(seft.bulletX, seft.bulletY, 5, 5)
    
    def update(self, x: int, y: int): 
        self.bulletX = x
        self.bulletY = y
        pygame.draw.circle(self.screen, (255,0,0), (self.bulletX, self.bulletY), 5)
        
            