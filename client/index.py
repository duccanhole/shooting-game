import pygame
import socket
from game_action import GAME_ACTION

from objects.tank import Tank
from utils.decode import decode


def initSocket():
    try:
        # # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # # Connect the socket to the server's address and port
        server_address = ("localhost", 8080)
        client_socket.connect(server_address)
        
        return (client_socket, client_socket.recv(1024))
    except:
        pass


def startGame(client_socket):
    pygame.init()

    screen_width = 700
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Shooting game")
    clock = pygame.time.Clock()

    tank1 = Tank(
        pygame,
        screen,
        client_socket,
        20,
        20,
        "tank1",
    )
    tank2 = Tank(
        pygame,
        screen,
        client_socket,
        screen_width - 20,
        screen_height - 20,
        "tank2",
    )
    try:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            screen.fill("white")

            tank1.addMovement()
            # tank1.addShooting()

            tank2.addMovement()
            # tank2.addHitting(tank1.bullet)

            # msg = decode(client_socket.recv(1024))
            # if len(msg) > 0:
            #     print(msg)
                # if msg.get("action") == GAME_ACTION.MOVE.value:
                #     data = msg.get("data")
                #     if data["name"] == "tank1":
                #         tank1.updateMovement(data["x"], data["y"])
                #     else:
                #         tank2.updateMovement(data["x"], data["y"])

            pygame.display.flip()
            clock.tick(60)

    # client_socket.close()
    finally:
        running = False
        # client_socket.close()
        pygame.quit()


def main():
    s = initSocket()
    startGame(s)


main()
