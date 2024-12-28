import pygame
import random

# Initialiser Pygame
pygame.init()

# Définir les couleurs
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Dimensions de la fenêtre
WIDTH = 500
HEIGHT = 500
BLOCK_SIZE = 20

# Définir la fenêtre du jeu
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-Man')

# Vitesse de Pac-Man
PACMAN_SPEED = 5

# Charger les images de Pac-Man (si vous en avez)
# Vous pouvez aussi dessiner Pac-Man avec pygame.draw.arc()

# Classe pour le labyrinthe
class Maze:
    def __init__(self):
        # Labyrinthe de base : 1 = mur, 0 = espace vide
        self.grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def draw(self):
        # Dessiner les murs
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(window, BLUE, [col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])

# Classe pour Pac-Man
class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.x += self.x_change
        self.y += self.y_change

        # Empêcher Pac-Man de sortir de l'écran
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH - BLOCK_SIZE:
            self.x = WIDTH - BLOCK_SIZE

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - BLOCK_SIZE:
            self.y = HEIGHT - BLOCK_SIZE

    def draw(self):
        pygame.draw.circle(window, YELLOW, (self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE // 2), BLOCK_SIZE // 2)

# Classe pour les fantômes
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(window, RED, [self.x, self.y, BLOCK_SIZE, BLOCK_SIZE])

# Boucle principale du jeu
def game_loop():
    pacman = PacMan(60, 60)
    ghost = Ghost(240, 240)
    maze = Maze()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.x_change = -PACMAN_SPEED
                    pacman.y_change = 0
                if event.key == pygame.K_RIGHT:
                    pacman.x_change = PACMAN_SPEED
                    pacman.y_change = 0
                if event.key == pygame.K_UP:
                    pacman.y_change = -PACMAN_SPEED
                    pacman.x_change = 0
                if event.key == pygame.K_DOWN:
                    pacman.y_change = PACMAN_SPEED
                    pacman.x_change = 0

        pacman.update()

        # Effacer l'écran et redessiner les éléments
        window.fill(BLACK)
        maze.draw()
        pacman.draw()
        ghost.draw()

        pygame.display.update()

        pygame.time.delay(100)

    pygame.quit()

# Lancer le jeu
game_loop()
