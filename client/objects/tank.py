import socket
import pygame

from game_action import GAME_ACTION
from objects.bullet import Bullet
from utils.encode import encode


class Tank:
    def __init__(
        self,
        context: pygame,
        screen: pygame.Surface,
        client_socket: socket,
        x,
        y,
        name="tank",
    ):
        self.context = context
        self.screen = screen
        self.tankX = x
        self.tankY = y
        self.speed = 5
        self.bullet = Bullet(context, screen)
        self.hp = 100
        self.name = name
        self.client_socket = client_socket

    def addMovement(self):
        # self.context.draw.circle(self.screen, (255,0,0), (self.tankX, self.tankY), 15)
        xData = self.tankX
        yData = self.tankY
        keys = self.context.key.get_pressed()
        if keys[pygame.K_a] and self.tankX >= 0:
            # self.tankX -= self.speed
            xData -= self.speed
        if keys[pygame.K_d] and self.tankX <= self.screen.get_width():
            # self.tankX += self.speed
            xData += self.speed
        if keys[pygame.K_w] and self.tankY >= 0:
            # self.tankY -= self.speed
            yData -= self.speed
        if keys[pygame.K_s] and self.tankY <= self.screen.get_height():
            # self.tankY += self.speed
            yData += self.speed
        if xData != self.tankX or yData != self.tankY:
            print('emit data')
            # sendData = {
            #     "action": GAME_ACTION.MOVE.value,
            #     "data": {"name": self.name, "x": xData, "y": yData},
            # }
            # self.client_socket.send(encode(sendData))

    def updateMovement(self, x: int, y: int):
        self.tankX = x
        self.tankY = y
        self.context.draw.circle(self.screen, (255, 0, 0), (self.tankX, self.tankY), 15)

    def addShooting(sefl):
        sefl.bullet.addFireAction()
        mouse = sefl.context.mouse.get_pressed()
        if mouse[0]:
            mouse_pos = sefl.context.mouse.get_pos()
            sefl.bullet.fire({"x": sefl.tankX, "y": sefl.tankY}, mouse_pos)

    def addHitting(self, bullet: Bullet):
        tankRect = pygame.Rect(self.tankX, self.tankY, 15, 15)
        bulletRect = bullet.getRect()
        collide = bulletRect.colliderect(tankRect)
        if collide:
            self.context.draw.circle(
                self.screen, (0, 0, 0), (self.tankX, self.tankY), 15
            )
            self.hp -= 1
            print("tank2 was shotting, hp: ", self.hp)
