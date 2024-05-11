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
pygame.display.set_caption("Hello pygame")
clock = pygame.time.Clock()

tank = Tank(pygame, screen ,screen_width / 2, screen_height / 2)


assets_path = os.path.join(os.path.dirname(__file__), '..', 'assets')


tank_img = pygame.image.load(os.path.join(assets_path, 'images', 'tank_img.jpg'))


scaled_tank_img = pygame.transform.scale(tank_img, (60, 60))  

dt = 2  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")  

    
    screen.blit(scaled_tank_img, (tank.position['x'] - scaled_tank_img.get_width() / 2, tank.position['y'] - scaled_tank_img.get_height() / 2))
    
    tank.addMovement()
    tank.addShooting()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
