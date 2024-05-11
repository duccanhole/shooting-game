import pygame
from objects.tank import Tank
import os
import socket

# # Create a TCP/IP socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect the socket to the server's address and port
# server_address = ("localhost", 8080)
# client_socket.connect(server_address)

pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting game")
clock = pygame.time.Clock()

tank1 = Tank(pygame, screen , 20 , 20)
tank2 = Tank(pygame, screen, screen_width - 20, screen_height - 20)

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
