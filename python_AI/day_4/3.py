import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("마우스를 따라가는 에이전트")

WHITE = (255, 255, 255)
BLUE = (0, 128, 255)

clock = pygame.time.Clock()
FPS = 60

agent_x = WIDTH // 2
agent_y = HEIGHT // 2
agent_radius = 20
agent_speed = 3

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx = mouse_x - agent_x
    dy = mouse_y - agent_y
    distance = math.hypot(dx, dy)

    if distance > 1:  # 너무 가까우면 멈춤
        dx /= distance
        dy /= distance

        # 3. ACT: 한 스텝씩 이동
        agent_x += dx * agent_speed
        agent_y += dy * agent_speed

    pygame.draw.circle(screen, BLUE, (int(agent_x), int(agent_y)), agent_radius)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()