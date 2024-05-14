import socket
import pygame

from network import Network
from game_action import GAME_ACTION
from objects.bullet import Bullet
from utils.encode import encode
from utils.decode import decode

CELL_SIZE = 40

class Tank:
    def __init__(
        self,
        screen: pygame.Surface,
        network: Network,
        x,
        y,
        player,
        currPlayer
    ):
        self.screen = screen
        self.tankX = x
        self.tankY = y
        self.speed = 5
        self.width = 20 
        self.height = 20
        self.bullet = Bullet(screen)
        self.hp = 100
        self.player = player
        self.currPlayer = currPlayer
        self.network = network
        
        
    def checkCollision(self, new_x, new_y, MAP):
        tank_rect = pygame.Rect(new_x, new_y, self.width, self.height)
        for y, row in enumerate(MAP):
            for x, cell in enumerate(row):
                if cell == 1:
                    wall_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    if tank_rect.colliderect(wall_rect):
                        return True
        return False
    
    
    def addMovement(self, MAP):
        if self.player == self.currPlayer:
            keys = pygame.key.get_pressed()
            new_x, new_y = self.tankX, self.tankY

            
            if keys[pygame.K_a] and self.tankX > 0:
                new_x -= self.speed
            if keys[pygame.K_d] and self.tankX + self.width < self.screen.get_width():
                new_x += self.speed
            if keys[pygame.K_w] and self.tankY > 0:
                new_y -= self.speed
            if keys[pygame.K_s] and self.tankY + self.height < self.screen.get_height():
                new_y += self.speed

            
            if not self.checkCollision(new_x, new_y, MAP):
                self.updateMovement(new_x, new_y)
            
    def updateMovement(self, x: int, y: int):
        self.tankX = x
        self.tankY = y
        pygame.draw.circle(self.screen, (255, 0, 0), (self.tankX, self.tankY), 15)

    def addShooting(sefl):
        if sefl.player == sefl.currPlayer:
            sefl.bullet.addFireAction()
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                mouse_pos = pygame.mouse.get_pos()
                sefl.bullet.fire({"x": sefl.tankX, "y": sefl.tankY}, mouse_pos)

    def addHitting(self, bullet: Bullet):
        tankRect = pygame.Rect(self.tankX, self.tankY, 15, 15)
        bulletRect = bullet.getRect()
        collide = bulletRect.colliderect(tankRect)
        if collide:
            pygame.draw.circle(
                self.screen, (0, 0, 0), (self.tankX, self.tankY), 15
            )
            self.hp -= 1
            print("tank2 was shotting, hp: ", self.hp)

    