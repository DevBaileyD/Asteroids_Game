import pygame 
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame verion {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Setting screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setting up FPS (Frames per second) how often our game updates
    clock = pygame.time.Clock()
    dt = 0.0

    # Creating groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    # instatiate main player & objects
    gamer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_objs = AsteroidField()

    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            collision = asteroid.collides_with(gamer)
            if collision:
                log_event("player_hit")
                print(f"Game Over!")
                sys.exit()
            

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
