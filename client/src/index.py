import pygame
from objects.tank import Tank
import os

pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello pygame")
clock = pygame.time.Clock()

tank1 = Tank(pygame, screen , 10 , 10)
tank2 = Tank(pygame, screen, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")  
    
    tank1.addMovement()
    tank1.addShooting()
    
    tank2.addMovement(False)
    tank2.addHitting(tank1.bullet)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
