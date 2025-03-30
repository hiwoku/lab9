import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 10

class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = "RIGHT"
        self.grow = False
    
    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            y += BLOCK_SIZE
        elif self.direction == "LEFT":
            x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            x += BLOCK_SIZE
        
        new_head = (x, y)
        if new_head in self.body or x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return False  
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True
    
    def change_direction(self, new_direction):
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction
    
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(SCREEN, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.timer = 300  
        self.value = random.randint(1, 3)
    
    def generate_position(self):
        return (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
    
    def reset(self):
        self.position = self.generate_position()
        self.timer = 300
        self.value = random.randint(1, 3)
    
    def draw(self):
        pygame.draw.rect(SCREEN, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))

snake = Snake()
food = Food()
score = 0
level = 1
running = True
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
while running:
    SCREEN.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
    
    if not snake.move():
        running = False  
    
    if snake.body[0] == food.position:
        score += food.value
        snake.grow = True
        food.reset()
        if score % 10 == 0:
            level += 1
            SPEED += 2
    
    food.timer -= 1
    if food.timer <= 0:
        food.reset()
    
    snake.draw()
    food.draw()
    
    score_text = font.render(f"Score: {score} Level: {level}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(SPEED)

pygame.quit()
