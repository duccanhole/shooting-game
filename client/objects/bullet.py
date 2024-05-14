import math
import pygame


class Bullet:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.bulletX = 0
        self.bulletY = 0
        self.isFiring = False
        self.angel = 0
        self.startPos = {'x': 0, 'y': 0}
        self.desPos = [0, 0]
        self.speed = 10
        
    def addFireAction(self):
        if self.isFiring: 
            if self.bulletX <= 0 or self.bulletX >= self.screen.get_width() or self.bulletY <= 0 or self.bulletY >= self.screen.get_height():
                self.bulletX = 0
                self.bulletY = 0
                self.isFiring = False 
            else: 
                dx = self.desPos[0] - self.startPos['x']
                dy = self.desPos[1] - self.startPos['y']
                if self.angel == 0: 
                    speedX = 0
                    speedY = self.speed
                elif abs(self.angel) == 1:
                    speedX = self.speed
                    speedY = 0
                elif self.angel > 45 and self.angel < 135: 
                    rad = math.radians(self.angel)
                    a = self.speed
                    h = a / math.sin(rad)
                    speedY = self.speed
                    speedX = math.sqrt(h**2 - a**2)
                else: 
                    rad = math.radians(self.angel)
                    a = self.speed
                    h = a / math.cos(rad)
                    speedX = self.speed
                    speedY = math.sqrt(h**2 - a**2)
                    
                if dx < 0: 
                    speedX *= -1
                if dy < 0:
                    speedY *= -1
                    
                self.bulletX += speedX
                self.bulletY += speedY
                pygame.draw.circle(self.screen, (255,0,0), (self.bulletX, self.bulletY), 5)
    
    def fire(self, startPos: dict, desPos: tuple):
        if self.isFiring == False:
            print('start fire ...')
            a = desPos[0] - startPos['x']
            b = desPos[1] - startPos['y']
            self.angel = math.degrees(math.acos(a / math.sqrt((a**2) + (b**2))))
            
            self.bulletX = startPos['x']
            self.bulletY = startPos['y']
            
            self.startPos = startPos
            self.desPos = desPos
            
            self.isFiring = True

    def getRect(seft): 
        return pygame.Rect(seft.bulletX, seft.bulletY, 5, 5)
    
    def update(self, x: int, y: int): 
        self.bulletX = x
        self.bulletY = y
        pygame.draw.circle(self.screen, (255,0,0), (self.bulletX, self.bulletY), 5)
        
            