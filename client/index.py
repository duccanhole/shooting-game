import pygame

from network import Network
from game_action import GAME_ACTION
from objects.tank import Tank
from utils.decode import decode

def startGame():
    currplayer = input("enter number : ")
    currplayer = int(currplayer)
    pygame.init()

    screen_width = 700
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Shooting game")
    clock = pygame.time.Clock()
    
    network = Network()

    tank1 = Tank(
        pygame,
        screen,
        network,
        20,
        20,
        1,
    )
    tank2 = Tank(
        pygame,
        screen,
        network,
        screen_width - 20,
        screen_height - 20,
        2,
    )
    try:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            screen.fill("white")

            tank1.addMovement(currplayer)
            # tank1.addShooting()

            # tank2.addMovement(currplayer)
            # tank2.addHitting(tank1.bullet)

            pygame.display.flip()
            clock.tick(60)

    # client_socket.close()
    finally:
        running = False
        # client_socket.close()
        pygame.quit()


def main():
    # s = initSocket()
    startGame()


main()