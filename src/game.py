import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save the Princess!")

# Load images
tower_img = pygame.image.load("tower.png")
witch_img = pygame.image.load("witch.png")
prince_img = pygame.image.load("prince.png")
apple_img = pygame.image.load("apple.png")
rapunzel_img = pygame.image.load("rapunzel.png")

class Tower:
    def __init__(self, x, y):
        self.image = tower_img
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Witch:
    def __init__(self, x, y):
        self.image = witch_img
        self.rect = self.image.get_rect(center=(x, y))
        self.cooldown = 0

    def update(self):
        if self.cooldown == 0:
            self.throw_apple()
            self.cooldown = FPS // 2
        else:
            self.cooldown -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def throw_apple(self):
        apple = Apple(self.rect.centerx, self.rect.bottom)
        apples.append(apple)

class Prince:
    def __init__(self, x, y):
        self.image = prince_img
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_up(self):
        self.rect.y -= 5

    def move_down(self):
        self.rect.y += 5

    def move_left(self):
        self.rect.x -= 5

    def move_right(self):
        self.rect.x += 5

class Apple:
    def __init__(self, x, y):
        self.image = apple_img
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        self.rect.y += 5

# Create game objects
tower = Tower(WIDTH // 2, 50)
witch = Witch(WIDTH // 2, 100)
prince = Prince(WIDTH // 2, HEIGHT - 50)
apples = []

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        prince.move_up()
    if keys[pygame.K_DOWN]:
        prince.move_down()
    if keys[pygame.K_LEFT]:
        prince.move_left()
    if keys[pygame.K_RIGHT]:
        prince.move_right()

    # Update
    witch.update()
    for apple in apples:
        apple.move()

    # Draw
    screen.fill(WHITE)
    tower.draw(screen)
    witch.draw(screen)
    prince.draw(screen)
    for apple in apples:
        screen.blit(apple.image, apple.rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
