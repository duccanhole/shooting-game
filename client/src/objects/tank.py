import math
import pygame

from objects.bullet import Bullet

class Tank:
    def __init__(self, x, y, speed=0.5, state=True):
        self.position = {'x': x, 'y': y}
    def __init__(self, context: pygame, screen: pygame.Surface, x, y, speed=5):
        self.context = context
        self.screen = screen
        self.tankX = x
        self.tankY = y
        self.speed = speed
        self.bullet = Bullet(context, screen)
        self.hp = 100

    def move(self, dx, dy):
        self.tankX += dx
        self.tankY += dy
        
    def addMovement(self, val: bool = True):
        self.context.draw.circle(self.screen, (255,0,0), (self.tankX, self.tankY), 15)
        if val: 
            keys = self.context.key.get_pressed()
            if keys[pygame.K_a] and self.tankX >= 0: 
                self.tankX -= self.speed
            if keys[pygame.K_d] and self.tankX <= self.screen.get_width():
                self.tankX += self.speed
            if keys[pygame.K_w] and self.tankY >= 0:
                self.tankY -= self.speed
            if keys[pygame.K_s] and self.tankY <= self.screen.get_height(): 
                self.tankY += self.speed
    
    def addShooting(sefl): 
        sefl.bullet.addFireAction()
        mouse = sefl.context.mouse.get_pressed()
        if mouse[0]:
            mouse_pos = sefl.context.mouse.get_pos()
            sefl.bullet.fire({ 'x': sefl.tankX, 'y': sefl.tankY }, mouse_pos)
    
    def addHitting(self, bullet: Bullet):
        tankRect = pygame.Rect(self.tankX, self.tankY, 15, 15)
        bulletRect = bullet.getRect()
        collide = bulletRect.colliderect(tankRect)
        if collide: 
            self.context.draw.circle(self.screen, (0,0,0), (self.tankX, self.tankY), 15)
            self.hp -= 1
            print("tank2 was shotting, hp: ", self.hp)