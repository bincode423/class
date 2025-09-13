import pygame
import time
import random
BLOCK_SIZE = 20
def draw_block_text(surface, text, start_x, start_y, color=(255, 255, 255)):
    FONT = {
        "A": [' ### ','#   #','#   #','#####','#   #','#   #','#   #'],
        "B": ['#### ','#   #','#   #','#### ','#   #','#   #','#### '],
        "C": [' ### ','#   #','#    ','#    ','#    ','#   #',' ### '],
        "D": ['#### ','#   #','#   #','#   #','#   #','#   #','#### '],
        "E": ['#####','#    ','#    ','#### ','#    ','#    ','#####'],
        "F": ['#####','#    ','#    ','#### ','#    ','#    ','#    '],
        "G": [' ### ','#   #','#    ','#  ##','#   #','#   #',' ### '],
        "H": ['#   #','#   #','#   #','#####','#   #','#   #','#   #'],
        "I": ['#####','  #  ','  #  ','  #  ','  #  ','  #  ','#####'],
        "J": ['#####','    #','    #','    #','    #','#   #',' ### '],
        "K": ['#   #','#  # ','# #  ','##   ','# #  ','#  # ','#   #'],
        "L": ['#    ','#    ','#    ','#    ','#    ','#    ','#####'],
        "M": ['#   #','## ##','# # #','# # #','#   #','#   #','#   #'],
        "N": ['#   #','##  #','##  #','# # #','#  ##','#  ##','#   #'],
        "O": [' ### ','#   #','#   #','#   #','#   #','#   #',' ### '],
        "P": ['#### ','#   #','#   #','#### ','#    ','#    ','#    '],
        "Q": [' ### ','#   #','#   #','#   #','# # #','#  # ',' ## #'],
        "R": ['#### ','#   #','#   #','#### ','# #  ','#  # ','#   #'],
        "S": [' ####','#    ','#    ',' ### ','    #','    #','#### '],
        "T": ['#####','  #  ','  #  ','  #  ','  #  ','  #  ','  #  '],
        "U": ['#   #','#   #','#   #','#   #','#   #','#   #',' ### '],
        "V": ['#   #','#   #','#   #','#   #','#   #',' # # ','  #  '],
        "W": ['#   #','#   #','#   #','# # #','# # #','## ##','#   #'],
        "X": ['#   #','#   #',' # # ','  #  ',' # # ','#   #','#   #'],
        "Y": ['#   #','#   #',' # # ','  #  ','  #  ','  #  ','  #  '],
        "Z": ['#####','    #','   # ','  #  ',' #   ','#    ','#####']
    }
    x_offset = 0
    for char in text.upper():
        if char in FONT:
            pattern = FONT[char]
            for row, line in enumerate(pattern):
                for col, pixel in enumerate(line):
                    if pixel == "#":
                        rect = pygame.Rect(
                            start_x + x_offset + col * BLOCK_SIZE,
                            start_y + row * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE
                        )
                        pygame.draw.rect(surface, color, rect)
            x_offset += (len(pattern[0]) + 1) * BLOCK_SIZE
        else:
            x_offset += 6 * BLOCK_SIZE


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PyGame")
running = True
x = 320
y = 240
clock = pygame.time.Clock()
btn = (20,0)
apple = (random.randint(0,620)//20*20,random.randint(0,460)//20*20)
score = 0
before = []


def ai_snake_direction(x, y, apple, before, score):
    """
    x, y : 뱀 머리 좌표
    apple : (x, y) 사과 좌표
    before : 뱀 몸 이동 기록 (머리 포함, 계속 축적 가능)
    score : 현재 뱀 길이
    """

    # 현재 뱀 몸 상태만 가져오기
    body = before[-score:]

    # 사과 우선 방향 후보
    directions = []
    if x > apple[0]:
        directions.append((-20, 0))
    elif x < apple[0]:
        directions.append((20, 0))
    if y > apple[1]:
        directions.append((0, -20))
    elif y < apple[1]:
        directions.append((0, 20))

    # 사과 방향 모두 막히면 fallback으로 다른 안전한 방향 시도
    fallback_dirs = [(-20,0), (20,0), (0,-20), (0,20)]

    # 먼저 사과 방향 중 안전한 것 선택
    for dx, dy in directions:
        next_pos = (x + dx, y + dy)
        if next_pos not in body:
            return (dx, dy)

    # 사과 방향 막히면 fallback 방향에서 안전한 것 선택
    for dx, dy in fallback_dirs:
        next_pos = (x + dx, y + dy)
        if next_pos not in body:
            return (dx, dy)

    # 혹시 모든 방향 막혀도, 무조건 한 칸 움직이게 마지막 fallback
    # 몸에 부딪혀도 어쩔 수 없이 진행
    dx, dy = fallback_dirs[0]
    return (dx, dy)

while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP] and y > 0:btn = (0,-20)
    # elif keys[pygame.K_DOWN] and y < 460:btn = (0,20)
    # elif keys[pygame.K_LEFT] and x > 0:btn = (-20,0)
    # elif keys[pygame.K_RIGHT] and x < 620:btn = (20,0)
    btn = ai_snake_direction(x, y, apple, before, score)
    x += btn[0]
    y += btn[1]
    if x < 0 or x > 620 or y < 0 or y > 460:
        running = False
    screen.fill((46,46,46))
    pygame.draw.rect(screen, (200,0,0),(apple[0], apple[1], 20, 20))
    pygame.draw.rect(screen, (0,200,0),(x, y, 20, 20))
    for i in range(score):
        pygame.draw.rect(screen, (0,0,200),(before[i][0], before[i][1], 20,20))
    before.insert(0,(x, y))
    if x == apple[0] and y == apple[1]:
        apple = (random.randint(0,620)//20*20,random.randint(0,460)//20*20)
        score += 1
    pygame.display.update()

draw_block_text(screen, "DIE", 150, 100, (255,0,0))
pygame.display.update()
pygame.time.wait(1000)
pygame.quit()