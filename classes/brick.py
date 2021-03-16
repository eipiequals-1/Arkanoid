import pygame, random
from .constants import *
from .GUI import HighScore, displayText



class Brick:
    SPACE = 4
    def __init__(self, color, x, y):
        self.color = color
        self.state = 'active'
        self.x = START_X + (CELL_W * x)
        self.y = START_Y + (CELL_H * y)
        self.w = CELL_W - self.SPACE
        self.h = CELL_H - self.SPACE
        self.rect = pygame.Rect(self.x + self.SPACE // 2, self.y + self.SPACE // 2, self.w, self.h)
        self.points = POINTS[self.color]

    def draw(self, surface):
        if self.state != 'destroyed':
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, BLACK, self.rect, 2)

            
    def checkHit(self, ball, game):
        if self.state != 'destroyed':
            collisionTolerance = 11
            if self.rect.colliderect(ball.rect):
                if abs(ball.rect.top - self.rect.bottom) < collisionTolerance and ball.vely < 0:
                    ball.vely *= -1
                    self.state = 'destroyed'
                    game.score += self.points
                if abs(ball.rect.bottom - self.rect.top) < collisionTolerance and ball.vely > 0:
                    ball.vely *= -1
                    self.state = 'destroyed'
                    game.score += self.points
                if abs(ball.rect.right - self.rect.left) < collisionTolerance and ball.velx > 0:
                    ball.velx *= -1
                    self.state = 'destroyed'
                    game.score += self.points
                if abs(ball.rect.left - self.rect.right) < collisionTolerance and ball.velx < 0:
                    ball.velx *= -1
                    self.state = 'destroyed'
                    game.score += self.points