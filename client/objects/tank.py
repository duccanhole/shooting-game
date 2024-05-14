import socket
import pygame

from network import Network
from game_action import GAME_ACTION
from objects.bullet import Bullet
from utils.encode import encode
from utils.decode import decode


class Tank:
    def __init__(
        self,
        context: pygame,
        screen: pygame.Surface,
        network: Network,
        x,
        y,
        player,
    ):
        self.context = context
        self.screen = screen
        self.tankX = x
        self.tankY = y
        self.speed = 5
        self.bullet = Bullet(context, screen)
        self.hp = 100
        self.player = player
        self.network = network

    def addMovement(self, curr):
        if self.player == curr:
            keys = self.context.key.get_pressed()
            if keys[pygame.K_a] and self.tankX >= 0:
                # self.tankX -= self.speed
                self.tankX -= self.speed
            if keys[pygame.K_d] and self.tankX <= self.screen.get_width():
                # self.tankX += self.speed
                self.tankX += self.speed
            if keys[pygame.K_w] and self.tankY >= 0:
                # self.tankY -= self.speed
                self.tankY -= self.speed
            if keys[pygame.K_s] and self.tankY <= self.screen.get_height():
                # self.tankY += self.speed
                self.tankY += self.speed
                # if xData != self.tankX or yData != self.tankY:
                #     self.updateMovement(xData, yData)
                #     print('emit data')
            self.updateMovement(self.tankX, self.tankY)
        # sendData = {
        #     "action": GAME_ACTION.MOVE.value,
        #     "data": {"player": self.player, "x": xData, "y": yData},
        # }
        # receiveData = self.network.send(sendData)
        # if self.player != curr:
        #     if len(receiveData) > 0:
        #         if receiveData.get("action") == GAME_ACTION.MOVE.value:
        #             data = receiveData.get("data")
        #             print("move, from receive data")
        #             self.updateMovement(data["x"], data["y"])
        #     else:
        #         print(f"update player {self.player} at ({xData}, {yData})")
        #         self.updateMovement(xData, yData)

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
