import pygame
import sys

# Khởi tạo Pygame
pygame.init()
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
# Kích thước của mỗi ô trong bản đồ
TILE_SIZE = 40

# Kích thước của màn hình
WIDTH = len(MAP[0]) * TILE_SIZE
HEIGHT = len(MAP) * TILE_SIZE

# Tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Bullet")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Bản đồ


# Tạo lớp đạn
class Bullet:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 5

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.collide_with_walls()

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

    def collide_with_walls(self):
        next_x = self.x + self.vx
        next_y = self.y + self.vy

        # Kiểm tra va chạm trái/phải
        if next_x - self.radius < 0 or next_x + self.radius > WIDTH or MAP[int(self.y / TILE_SIZE)][int(next_x / TILE_SIZE)] == 1:
            self.vx = -self.vx
        # Kiểm tra va chạm trên/dưới
        if next_y - self.radius < 0 or next_y + self.radius > HEIGHT or MAP[int(next_y / TILE_SIZE)][int(self.x / TILE_SIZE)] == 1:
            self.vy = -self.vy

# Tạo đạn ban đầu
bullet = Bullet(TILE_SIZE * 2, TILE_SIZE * 2, 5, 5)

# Vòng lặp chính
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật đạn
    bullet.update()

    # Vẽ lên màn hình
    screen.fill(BLACK)

    # Vẽ bản đồ
    for row in range(len(MAP)):
        for col in range(len(MAP[row])):
            if MAP[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Vẽ đạn
    bullet.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
