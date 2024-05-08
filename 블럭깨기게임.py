import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 패들 설정
paddle_width = 120
paddle_height = 20
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - 50
paddle_speed = 10

# 공 설정
ball_radius = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 5 * random.choice([-1, 1])
ball_dy = 5
ball_speed = 5

# 벽돌 설정
brick_width = 80
brick_height = 30
brick_cols = SCREEN_WIDTH // brick_width
brick_rows = 4
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height + 50
        brick_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - paddle_width:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 공과 벽 충돌 처리
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= SCREEN_WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius <= 0:
        ball_dy = -ball_dy

    # 패들과 공 충돌 처리
    if ball_y + ball_radius >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width and ball_dy > 0:
        ball_dy = -ball_dy

    # 벽돌과 공 충돌 처리
    for brick in bricks:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy = -ball_dy

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)

    pygame.display.flip()

    # 게임 오버 조건
    if ball_y - ball_radius > SCREEN_HEIGHT:
        font = pygame.font.Font(None, 74)
        text = font.render("게임 오버", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    if not bricks:
        font = pygame.font.Font(None, 74)
        text = font.render("승리!", True, BLUE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    clock.tick(30)  # FPS를 30으로 변경 (초당 30프레임)

pygame.quit()
