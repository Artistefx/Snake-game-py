import pygame
import sys
import time
import random

# Initialize pygame
pygame.init()

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up game window
frame_size_x = 1280
frame_size_y = 720
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Snake Game")
fps_controller = pygame.time.Clock()
square_size = 60

# Initialize game variables
speed = 10
direction = "RIGHT"
head_pos = [120, 60]
snake_body = [[120, 60]]
food_pos = [random.randrange(1, frame_size_x // square_size) * square_size,
            random.randrange(1, frame_size_y // square_size) * square_size]
food_spawn = True
score = 0
game_over = False

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect(midtop=(frame_size_x / 10, 15))
    game_window.blit(score_surface, score_rect)

def game_over_screen():
    my_font = pygame.font.Font(None, 50)
    game_over_surface = my_font.render("GAME OVER - Your score is: " + str(score), True, red)
    game_over_rect = game_over_surface.get_rect(midtop=(frame_size_x / 2, frame_size_y / 4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("w")) and direction != "DOWN":
                direction = "UP"
            elif (event.key == pygame.K_DOWN or event.key == ord("s")) and direction != "UP":
                direction = "DOWN"
            elif (event.key == pygame.K_LEFT or event.key == ord("a")) and direction != "RIGHT":
                direction = "LEFT"
            elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and direction != "LEFT":
                direction = "RIGHT"

    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size

    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    snake_body.insert(0, list(head_pos))

    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, frame_size_x // square_size) * square_size,
                    random.randrange(1, frame_size_y // square_size) * square_size]
        food_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0] + 2, pos[1] + 2, square_size - 2, square_size - 2))
    
    pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], square_size, square_size))

    for block in snake_body[1:]:
        if head_pos == block:
            game_over = True
            break

    show_score(white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(speed)

game_over_screen()
import pygame
import sys
import time
import random

# Initialize pygame
pygame.init()

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up game window
frame_size_x = 1280
frame_size_y = 720
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Snake Game")
fps_controller = pygame.time.Clock()
square_size = 60

# Initialize game variables
speed = 10
direction = "RIGHT"
head_pos = [120, 60]
snake_body = [[120, 60]]
food_pos = [random.randrange(1, frame_size_x // square_size) * square_size,
            random.randrange(1, frame_size_y // square_size) * square_size]
food_spawn = True
score = 0
game_over = False

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect(midtop=(frame_size_x / 10, 15))
    game_window.blit(score_surface, score_rect)

def game_over_screen():
    my_font = pygame.font.Font(None, 50)
    game_over_surface = my_font.render("GAME OVER - Your score is: " + str(score), True, red)
    game_over_rect = game_over_surface.get_rect(midtop=(frame_size_x / 2, frame_size_y / 4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("w")) and direction != "DOWN":
                direction = "UP"
            elif (event.key == pygame.K_DOWN or event.key == ord("s")) and direction != "UP":
                direction = "DOWN"
            elif (event.key == pygame.K_LEFT or event.key == ord("a")) and direction != "RIGHT":
                direction = "LEFT"
            elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and direction != "LEFT":
                direction = "RIGHT"

    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size

    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    snake_body.insert(0, list(head_pos))

    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, frame_size_x // square_size) * square_size,
                    random.randrange(1, frame_size_y // square_size) * square_size]
        food_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0] + 2, pos[1] + 2, square_size - 2, square_size - 2))
    
    pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], square_size, square_size))

    for block in snake_body[1:]:
        if head_pos == block:
            game_over = True
            break

    
    show_score(white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(speed)

game_over_screen()

    
        