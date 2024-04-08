import pygame
from objects.tank import Tank
import os

pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello pygame")
clock = pygame.time.Clock()

tank = Tank(screen_width / 2, screen_height / 2)


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

    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_w]:
        dy -= 5 * dt
    if keys[pygame.K_s]:
        dy += 5 * dt
    if keys[pygame.K_a]:
        dx -= 5 * dt
    if keys[pygame.K_d]:
        dx += 5 * dt

    tank.move(dx, dy)  
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    angle = tank.get_angle(tank.position['x'], tank.position['y'], mouse_x, mouse_y)
    
    
    rotated_tank = pygame.transform.rotate(scaled_tank_img, -angle)
    rotated_rect = rotated_tank.get_rect(center=(tank.position['x'], tank.position['y']))
    screen.blit(rotated_tank, rotated_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
