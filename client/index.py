import pygame

from network import Network
from game_action import GAME_ACTION
from objects.tank import Tank
from utils.decode import decode
from utils.encode import encode

def drawMap(screen):
    # Kích thước ô vuông trên bản đồ
    CELL_SIZE = 40
    # Màu sắc
    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)
    # Ma trận đại diện cho bản đồ, số 1 là bức tường
    MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
    # Vẽ bản đồ
    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def startGame():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Shooting game")
    clock = pygame.time.Clock()

    network = Network()

    currPlayer = network.getStartData()["data"]["currPlayer"]

    print(f"Your player id {currPlayer}")

    tank0 = Tank(
        screen,
        network,
        60,
        60,
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
            
            drawMap(screen)

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
