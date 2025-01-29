import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()  # Create a new pygame.time.Clock object
    dt = 0  # Initialize dt variable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Control the frame rate and update dt

if __name__ == "__main__":
    main()