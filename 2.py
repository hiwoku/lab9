import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
color = BLACK
mode = "circle"
start_pos = None

while running:
    SCREEN.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = GREEN
            elif event.key == pygame.K_3:
                color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos
            if mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(SCREEN, color, start_pos, radius, 2)
            elif mode == "rectangle":
                pygame.draw.rect(SCREEN, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "square":
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(SCREEN, color, (*start_pos, side, side), 2)
            elif mode == "triangle":
                pygame.draw.polygon(SCREEN, color, [start_pos, (end_pos[0], start_pos[1]), ((start_pos[0] + end_pos[0]) // 2, end_pos[1])], 2)
            elif mode == "rhombus":
                center_x = (start_pos[0] + end_pos[0]) // 2
                center_y = (start_pos[1] + end_pos[1]) // 2
                dx = abs(end_pos[0] - start_pos[0]) // 2
                dy = abs(end_pos[1] - start_pos[1]) // 2
                pygame.draw.polygon(SCREEN, color, [(center_x, start_pos[1]), (end_pos[0], center_y), (center_x, end_pos[1]), (start_pos[0], center_y)], 2)
    
    pygame.display.update()

pygame.quit()