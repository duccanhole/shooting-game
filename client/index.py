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
        screen,
        network,
        20,
        20,
        0,
        currPlayer
    )
    tank1 = Tank(
        screen,
        network,
        screen_width - 20,
        screen_height - 20,
        1,
        currPlayer
    )
    try:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            screen.fill("white")

            tank0.addMovement()
            tank0.addShooting()

            tank1.addMovement()
            tank1.addShooting()
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
                    if data["player"] == 0:
                        tank0.updateMovement(data["x"], data["y"])
                    else:
                        tank1.updateMovement(data["x"], data["y"])
                        
            sendBulletData = {
                "action": GAME_ACTION.FIRE.value,
                "data": {
                    "player": 1 if currPlayer == 1 else 0,
                    "x": tank1.bullet.bulletX if currPlayer == 1 else tank0.bullet.bulletX,
                    "y": tank1.bullet.bulletY if currPlayer == 1 else tank0.bullet.bulletY,
                }
            }
            receiveBulletData = network.send(sendBulletData)
            if len(receiveBulletData) > 0:
                if receiveBulletData.get("action") == GAME_ACTION.FIRE.value:
                    data = receiveBulletData.get("data")
                    if data["player"] == 0:
                        tank0.bullet.update(data["x"], data["y"])
                    else:
                        tank1.bullet.update(data["x"], data["y"])

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
