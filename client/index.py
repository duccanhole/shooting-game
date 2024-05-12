import pygame

from network import Network
from game_action import GAME_ACTION
from objects.tank import Tank
from utils.decode import decode
from utils.encode import encode


def startGame():
    pygame.init()

    screen_width = 700
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Shooting game")
    clock = pygame.time.Clock()

    network = Network()

    currPlayer = network.getStartData()["data"]["currPlayer"]

    print(f"Your player id {currPlayer}")

    tank0 = Tank(
        pygame,
        screen,
        network,
        20,
        20,
        0,
    )
    tank1 = Tank(
        pygame,
        screen,
        network,
        screen_width - 20,
        screen_height - 20,
        1,
    )
    try:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            screen.fill("white")

            tank0.addMovement(currPlayer)
            # tank1.addShooting()

            tank1.addMovement(currPlayer)
            # tank2.addHitting(tank1.bullet)

            sendMoveData = {
                "action": GAME_ACTION.MOVE.value,
                "data": {
                    "player": 1 if currPlayer == 1 else 0,
                    "x": tank1.tankX if currPlayer == 1 else tank0.tankX,
                    "y": tank1.tankY if currPlayer == 1 else tank0.tankY,
                },
            }
            receiveMoveData = network.send(sendMoveData)
            if len(receiveMoveData) > 0:
                if receiveMoveData.get("action") == GAME_ACTION.MOVE.value:
                    data = receiveMoveData.get("data")
                    print("move, from receive data")
                    if data["player"] == 0:
                        tank0.updateMovement(data["x"], data["y"])
                    else:
                        tank1.updateMovement(data["x"], data["y"])

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