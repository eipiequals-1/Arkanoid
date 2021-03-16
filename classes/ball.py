import pygame, random
from .constants import B_RECT, HEIGHT, F_GREEN


class Ball:
    """
    The ball object checks for collisions with the walls and takes away lives accordingly.
    It moves based off of constant velocities."""
    def __init__(self, x, y, w, h):
        self.reset(x, y, w, h)
        self.color = (200, 200, 200)

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)
        pygame.draw.ellipse(surface, F_GREEN, self.rect, 3)

    def reset(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.velx = random.choice([7, -7])  # reset the ball to the left or the right
        self.vely = -7  # Y velocity constant

    def update(self, surface, x, y, w, h, game):
        self.draw(surface)
        self.rect.x += self.velx
        self.rect.y += self.vely

        # checks wall collisions
        if (self.rect.left <= B_RECT.left and self.velx < 0) or (self.rect.right >= B_RECT.right and self.velx > 0):
            self.velx *= -1
        elif (self.rect.top <= B_RECT.top and self.vely < 0):
            self.vely *= -1

        # events that happen when ball goes outside the borders
        elif (self.rect.bottom > HEIGHT):
            self.reset(x, y, w, h)
            game.lives -= 1


