import pygame

from network import Network
from game_action import GAME_ACTION
from objects.tank import Tank

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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def drawMap(screen):

    CELL_SIZE = 40

    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)

    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(
                    screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )


def drawScrore(screen: pygame.Surface, myScore, otherScore):
    text_color = (255, 255, 255)
    text = f"Your score: {myScore} - Opponent score: {otherScore}"
    font = pygame.font.Font(None, 25)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() / 2, 15)
    screen.blit(text_surface, text_rect)


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

    tank0 = Tank(screen, network, 60, 60, 0, currPlayer)
    tank1 = Tank(
        screen, network, screen_width - 100, screen_height - 100, 1, currPlayer
    )

    tank0Score = 0
    tank1Score = 0
    try:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            if tank0Score == 10 or tank1Score == 10:
                screen.fill("black")
                text = ""
                if tank0Score == 10 and currPlayer == 0:
                    text = "You win !!!"
                else:
                    text = "You lose !!!"
                text_color = (255, 255, 255)
                font = pygame.font.Font(None, 75)
                text_surface = font.render(text, True, text_color)
                text_rect = text_surface.get_rect()
                text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
                clock.tick(60)
                continue

            screen.fill("white")

            drawMap(screen)

            tank0.addMovement(MAP)
            tank0.addShooting()
            isTank0Hitting = tank0.addHitting(tank1.bullet)

            tank1.addMovement(MAP)
            tank1.addShooting()
            isTank1Hitting = tank1.addHitting(tank0.bullet)

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
                    "x": (
                        tank1.bullet.bulletX
                        if currPlayer == 1
                        else tank0.bullet.bulletX
                    ),
                    "y": (
                        tank1.bullet.bulletY
                        if currPlayer == 1
                        else tank0.bullet.bulletY
                    ),
                },
            }
            receiveBulletData = network.send(sendBulletData)
            if len(receiveBulletData) > 0:
                if receiveBulletData.get("action") == GAME_ACTION.FIRE.value:
                    data = receiveBulletData.get("data")
                    if data["player"] == 0:
                        tank0.bullet.update(data["x"], data["y"])
                        if data["x"] + data["y"] == 0:
                            tank0.bullet.isFiring = False
                    else:
                        tank1.bullet.update(data["x"], data["y"])
                        if data["x"] + data["y"] == 0:
                            tank1.bullet.isFiring = False

            sendScoreData = {
                "action": GAME_ACTION.SCORE.value,
                "data": [tank0Score, tank1Score],
            }
            if isTank0Hitting:
                sendScoreData["data"][1] += 1
            if isTank1Hitting:
                sendScoreData["data"][0] += 1
            receiveScoreData = network.send(sendScoreData)
            if len(receiveScoreData) > 0:
                if receiveScoreData.get("action") == GAME_ACTION.SCORE.value:
                    data = receiveScoreData.get("data")
                    if data[0] != tank0Score or data[1] != tank1Score:
                        pygame.time.wait(1000)
                        tank0Score = data[0]
                        tank1Score = data[1]
                        tank0.updateMovement(60, 60)
                        tank0.bullet.update(0, 0)
                        tank0.bullet.isFiring = False
                        tank1.updateMovement(700, 500)
                        tank1.bullet.update(0, 0)
                        tank1.bullet.isFiring = False

            drawScrore(
                screen,
                tank0Score if currPlayer == 0 else tank1Score,
                tank1Score if currPlayer == 0 else tank0Score,
            )

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
