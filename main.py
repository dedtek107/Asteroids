import pygame

#import everything from constants.py
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000.0
    

if __name__ == "__main__":
    main()
