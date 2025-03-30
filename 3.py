import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
coin_img = pygame.image.load("coin.png")

player_img = pygame.transform.scale(player_img, (50, 100))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))
coin_img = pygame.transform.scale(coin_img, (20, 20))

running = True
player_x, player_y = WIDTH // 2, HEIGHT - 100
player_speed = 5
enemy_x, enemy_y = random.randint(0, WIDTH - 50), -100
enemy_speed = 5
coins = []
score = 0

def generate_coin():
    return [random.randint(0, WIDTH - 20), random.randint(-200, -20), random.randint(1, 3)]

for _ in range(5):
    coins.append(generate_coin())

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
while running:
    SCREEN.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - 50)
    
    for coin in coins:
        coin[1] += 3
        if coin[1] > HEIGHT:
            coin[:] = generate_coin()
    
    for coin in coins:
        if player_x < coin[0] < player_x + 50 and player_y < coin[1] < player_y + 50:
            score += coin[2]
            coin[:] = generate_coin()
    
    if score >= 10:
        enemy_speed = 7
    if score >= 20:
        enemy_speed = 9
    
    SCREEN.blit(player_img, (player_x, player_y))
    SCREEN.blit(enemy_img, (enemy_x, enemy_y))
    for coin in coins:
        SCREEN.blit(coin_img, (coin[0], coin[1]))
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
