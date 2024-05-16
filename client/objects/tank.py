import math
import socket
import pygame

from network import Network
from game_action import GAME_ACTION
from objects.bullet import Bullet
from utils.encode import encode
from utils.decode import decode

CELL_SIZE = 40
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
class Tank:
    def __init__(
        self, screen: pygame.Surface, network: Network, x, y, player, currPlayer
    ):
        self.screen = screen
        self.tankX = x
        self.tankY = y
        self.speed = 2
        self.width = 20 
        self.height = 20
        self.bullet = Bullet(screen)
        self.player = player
        self.currPlayer = currPlayer
        self.network = network

    def checkCollision(self, new_x, new_y, MAP):
        tank_rect = pygame.Rect(new_x, new_y, self.width + 10, self.height + 10)
        for y, row in enumerate(MAP):
            for x, cell in enumerate(row):
                if cell == 1:
                    wall_rect = pygame.Rect(
                        x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE
                    )
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
            self.updateMovement(self.tankX, self.tankY)

    def updateMovement(self, x: int, y: int):
        self.tankX = x
        self.tankY = y
        pygame.draw.circle(
            self.screen, (255, 0, 0), (self.tankX + 15, self.tankY + 15), 15
        )

    def addShooting(self):
        if self.player == self.currPlayer:
            self.bullet.addFireAction(MAP)
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                mouse_pos = pygame.mouse.get_pos()
                self.bullet.fire({"x": self.tankX+ self.width // 2, "y": self.tankY+ self.height // 2}, mouse_pos)

    def addHitting(self, bullet: Bullet):
        # tankRect = pygame.Rect(self.tankX, self.tankY, self.width + 5, self.height + 5)
        # bulletRect = bullet.getRect()
        # collide = bulletRect.colliderect(tankRect)
        distance = math.sqrt((self.tankX + 15 - bullet.bulletX) ** 2 + (self.tankY + 15 - bullet.bulletY) ** 2)
        collide = distance <= (10 + 5)
        return collide