import pygame
from objects.tank import Tank

pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello pygame")
clock = pygame.time.Clock()

tank = Tank(screen_width / 2, screen_height / 2, direction='right', rotationAngle="a")
dt = 2  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 0, 128))  

    pygame.draw.circle(screen, (255, 0, 0), (int(tank.position['x']), int(tank.position['y'])), 40)

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
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
