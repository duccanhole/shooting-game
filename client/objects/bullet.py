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
        self.speed = 1
        self.fire_time = None
        
    def addFireAction(self, MAP):
        if self.isFiring: 
            current_time = time.time()
            if (current_time - self.fire_time) > 7:  
                self.isFiring = False
                    
            # Tính toán chỉ số của ô trong bản đồ
            map_x = int(self.bulletX // CELL_SIZE)
            map_y = int(self.bulletY // CELL_SIZE)
            
            
            if map_x >= 0 and map_x < len(MAP[0]) and map_y >= 0 and map_y < len(MAP):
                if MAP[map_y][map_x] == 1:
                    # Xác định hướng va chạm
                    if abs(self.speedX) > abs(self.speedY):  
                        print("(" + str(self.speedX) + "," + str(self.speedY) + ")")
                        self.speedX *= -1
                    else:  
                        print("(" + str(self.speedX) + "," + str(self.speedY) + ")")
                        self.speedY *= -1
                        
                    if self.speedX < 0:
                        self.bulletX = map_x * CELL_SIZE -10
                    else:
                        self.bulletX = (map_x + 1) * CELL_SIZE + 10
                        
                    if self.speedY < 0:
                        self.bulletY = map_y * CELL_SIZE - 10
                    else:
                        self.bulletY = (map_y + 1) * CELL_SIZE + 10
                        
                    if MAP[int(self.bulletY // CELL_SIZE)][map_x] == 1:
                        self.isFiring = False
                else:
                    self.bulletX += self.speedX
                    self.bulletY += self.speedY
                
   
            pygame.draw.circle(self.screen, (255, 0, 0), (int(self.bulletX), int(self.bulletY)), 10)
            
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
        
            