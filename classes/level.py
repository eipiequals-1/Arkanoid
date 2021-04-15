import pygame

from .brick import Brick
from .constants import *

class Level:
    def __init__(self, levelNum):
        self.initialize(levelNum)
                        
    def draw(self, surface):
        for brick in self.bricks:
            brick.draw(surface)

    def update(self, surface, ball, game, highScore):
        self.draw(surface)
        for brick in self.bricks:
            brick.checkHit(ball, game)

        for index, brick in enumerate(self.bricks):
            if brick.state == "destroyed":
                self.bricks.pop(index)

        high = highScore.getMax()
            
        font = pygame.font.SysFont("uroob", 35)
        writing1 = font.render("Score: " + str(game.score), 1, RED)
        writing2 = font.render("Lives: " + str(game.lives), 1, RED)
        writing3 = font.render("High Score: " + str(high), 1, RED)
        surface.blit(writing1, (B_RECT.left + 10, B_RECT.top - 75))
        surface.blit(writing2, ((WIDTH - writing2.get_width()) // 2, B_RECT.top - 75))
        surface.blit(writing3, (B_RECT.right - 10 - writing3.get_width(), B_RECT.top - 75))

    def initialize(self, levelNum):
        self.bricks = []
        for y, line in enumerate(LEVELS[levelNum - 1]):
            for x, char in enumerate(line):
                if char != " ":
                    self.bricks.append(Brick(COLORS[char], x, y))

    def getWin(self):
        return len(self.bricks) == 0
    
    def getLose(self, game):
        return game.lives <= 0


