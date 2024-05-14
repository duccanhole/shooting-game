import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ game và kích thước của ô vuông trên bản đồ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40

# Kích thước bản đồ (số hàng và số cột)
MAP_WIDTH = 20
MAP_HEIGHT = 15

# Tính toán kích thước thực của bản đồ
MAP_WIDTH_PIXELS = MAP_WIDTH * CELL_SIZE
MAP_HEIGHT_PIXELS = MAP_HEIGHT * CELL_SIZE

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

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

# Khởi tạo cửa sổ game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Game")

# Hình chữ nhật đại diện cho xe tăng
tank_width = 20
tank_height = 20
tank_x = 200
tank_y = 200

# Vận tốc di chuyển của xe tăng
tank_speed = 5

# Vẽ bản đồ
def draw_map():
    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Vẽ xe tăng
def draw_tank(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, tank_width, tank_height))
    pygame.draw.circle(screen, RED, (x + tank_width // 2, y + tank_height // 2), tank_width // 2)

# Vòng lặp game
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Xử lý phím điều khiển
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank_x -= tank_speed
    if keys[pygame.K_RIGHT]:
        tank_x += tank_speed
    if keys[pygame.K_UP]:
        tank_y -= tank_speed
    if keys[pygame.K_DOWN]:
        tank_y += tank_speed

    # Giới hạn vị trí của xe tăng trong cửa sổ game
    tank_x = max(0, min(MAP_WIDTH_PIXELS - tank_width, tank_x))
    tank_y = max(0, min(MAP_HEIGHT_PIXELS - tank_height, tank_y))

    # Xóa màn hình
    screen.fill(WHITE)

    # Vẽ bản đồ
    draw_map()

    # Vẽ xe tăng
    draw_tank(tank_x, tank_y)

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình
    pygame.time.Clock().tick(60)
