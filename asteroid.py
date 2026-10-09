import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            # creating parameters for smaller split asteroids
            new_vector = self.velocity.rotate(random.uniform(20, 50))
            neg_new_vector = self.velocity.rotate(random.uniform(20, 50)*-1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create new smaller asteroids
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            # set new asteroids velocity's 
            new_asteroid_1.velocity = new_vector * 1.2
            new_asteroid_2.velocity = neg_new_vector * 1.2 
