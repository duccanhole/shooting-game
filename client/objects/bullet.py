import math
import time
import pygame
from setting import MAP, CELL_SIZE

WIDTH = len(MAP[0]) * CELL_SIZE
HEIGHT = len(MAP) * CELL_SIZE
class Bullet:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.bulletX = 0
        self.bulletY = 0
        self.isFiring = False
        self.angel = 0
        self.startPos = {'x': 0, 'y': 0}
        self.desPos = [0, 0]
        self.speed = 6
        self.fire_time = None
        
    def addFireAction(self, MAP):
        if self.isFiring: 
            current_time = time.time()
            if (current_time - self.fire_time) > 5:  
                self.isFiring = False
                    
            next_x = self.bulletX + self.speedX
            next_y = self.bulletY + self.speedY

            # Kiểm tra va chạm trái/phải
            if next_x - 5 < 0 or next_x + 5 > WIDTH or MAP[int(self.bulletY / CELL_SIZE)][int(next_x / CELL_SIZE)] == 1:
                self.speedX = -self.speedX
            # Kiểm tra va chạm trên/dưới
            if next_y - 5 < 0 or next_y + 5 > HEIGHT or MAP[int(next_y / CELL_SIZE)][int(self.bulletX / CELL_SIZE)] == 1:
                self.speedY = -self.speedY
                
            self.bulletX += self.speedX
            self.bulletY += self.speedY
            pygame.draw.circle(self.screen, (255, 0, 0), (int(self.bulletX), int(self.bulletY)), 5)
            
    def fire(self, startPos: dict, desPos: tuple):
        if not self.isFiring:
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
        
            