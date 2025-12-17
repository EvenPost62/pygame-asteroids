import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

pygame.init()

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #screen defined
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #gameclock setup
    gameclock = pygame.time.Clock()
    dt = 0

    #instance player object centred
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    

    
    #game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = gameclock.tick(60)/1000 #seconds per frame - i.e. 16.67 ms for 60 fps


if __name__ == "__main__":
    main()
