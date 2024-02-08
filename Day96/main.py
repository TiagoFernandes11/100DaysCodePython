import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Shooter")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 10

# Set up bullet
bullet_size = 5
bullet_speed = 7
bullet_state = "ready"  # "ready" or "fire"
bullet_x = 0
bullet_y = 0

# Set up alien
alien_size = 50
alien_speed = 2
alien_x = random.randint(0, WIDTH - alien_size)
alien_y = 0

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # Fire bullet
        if keys[pygame.K_SPACE] and bullet_state == "ready":
            bullet_state = "fire"
            bullet_x = player_x + player_size // 2
            bullet_y = player_y - bullet_size

    # Move bullet
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = "ready"

    # Move alien
    alien_y += alien_speed
    if alien_y > HEIGHT:
        alien_x = random.randint(0, WIDTH - alien_size)
        alien_y = 0

    # Collision detection
    if (
        player_x < alien_x + alien_size
        and player_x + player_size > alien_x
        and player_y < alien_y + alien_size
        and player_y + player_size > alien_y
    ):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Bullet-alien collision detection
    if (
        bullet_x < alien_x + alien_size
        and bullet_x + bullet_size > alien_x
        and bullet_y < alien_y + alien_size
        and bullet_y + bullet_size > alien_y
    ):
        alien_x = random.randint(0, WIDTH - alien_size)
        alien_y = 0
        bullet_state = "ready"

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (alien_x, alien_y, alien_size, alien_size))
    pygame.draw.circle(
        screen, RED, (bullet_x + bullet_size // 2, bullet_y + bullet_size // 2), bullet_size // 2
    )

    pygame.display.flip()
    clock.tick(30)
