import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))  # Green tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # Tower logic goes here
        pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))  # Red enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 4)

def game_loop():
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    towers = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Create the player's tower
    tower = Tower(WIDTH // 2, HEIGHT - 50)
    all_sprites.add(tower)
    towers.add(tower)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game objects
        all_sprites.update()

        # Draw the game
        window.fill(WHITE)
        all_sprites.draw(window)

        # Update the display
        pygame.display.flip()

        # Set the desired frames per second (FPS)
        clock = pygame.time.Clock()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
