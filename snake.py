import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game window
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Clock & Font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Snake settings
snake = [(100, 100)]
direction = (CELL_SIZE, 0)
speed = 10

# Food
def spawn_food():
    while True:
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        if food not in snake:
            return food

food = spawn_food()

# Draw
def draw_snake():
    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def show_score():
    score_text = font.render(f"Score: {len(snake) - 1}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop
def game_loop():
    global direction, food, snake
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        # Move snake
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Collision check
        if (new_head in snake or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        # Eating food
        if new_head == food:
            food = spawn_food()
        else:
            snake.pop()

        draw_snake()
        draw_food()
        show_score()
        pygame.display.update()
        clock.tick(speed)

# Start game
game_loop()
# Quit Pygame