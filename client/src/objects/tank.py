import math
import pygame

from objects.bullet import Bullet

class Tank:
    def __init__(self, x, y, speed=0.5, state=True):
        self.position = {'x': x, 'y': y}
        self.speed = speed
        self.state = state
        self.bullet = Bullet(context, screen)

    def move(self, dx, dy):
        self.position['x'] += dx
        self.position['y'] += dy
        
    def addMovement(self): 
        keys = self.context.key.get_pressed()
        if keys[pygame.K_a]:
            self.position['x'] -= self.speed
        if keys[pygame.K_d]:
            self.position['x'] += self.speed
        if keys[pygame.K_w]:
            self.position['y'] -= self.speed
        if keys[pygame.K_s]: 
            self.position['y'] += self.speed
    
    def addShooting(sefl): 
        sefl.bullet.addFireAction()
        mouse = sefl.context.mouse.get_pressed()
        if mouse[0]:
            mouse_pos = sefl.context.mouse.get_pos()
            sefl.bullet.fire(sefl.position, mouse_pos)