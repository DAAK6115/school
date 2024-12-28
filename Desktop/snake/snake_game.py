import pygame
import time
import random

# Initialiser Pygame
pygame.init()

# Définir les couleurs
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Dimensions de la fenêtre du jeu
WIDTH = 600
HEIGHT = 400

# Définir la taille des blocs (taille de la tête du serpent)
BLOCK_SIZE = 10
SNAKE_SPEED = 15

# Définir la fenêtre du jeu
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Définir le temps pour le jeu
clock = pygame.time.Clock()

# Définir la police pour le score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Variable pour stocker le score le plus élevé
high_score = 0

# Fonction pour afficher le score
def display_score(score, high_score):
    value = score_font.render(f"Score: {score}  High Score: {high_score}", True, YELLOW)
    window.blit(value, [0, 0])

# Fonction pour dessiner le serpent
def draw_snake(block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(window, GREEN, [block[0], block[1], block_size, block_size])

# Fonction pour afficher un message
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Boucle principale du jeu
def game_loop():
    global high_score  # Utiliser la variable globale pour le score le plus élevé
    game_over = False
    game_close = False

    # Coordonnées initiales du serpent
    x = WIDTH / 2
    y = HEIGHT / 2

    # Changement de direction
    x_change = 0
    y_change = 0

    # Corps du serpent
    snake_body = []
    snake_length = 1

    # Position de la nourriture
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(BLUE)
            display_message("Game Over! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(BLUE)

        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_body)
        display_score(snake_length - 1, high_score)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    # Mettre à jour le score le plus élevé
    if snake_length - 1 > high_score:
        high_score = snake_length - 1

    pygame.quit()
    quit()

# Lancer le jeu
game_loop()
