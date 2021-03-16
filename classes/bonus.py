import pygame, random
from .constants import WIDTH, HEIGHT, WHITE, B_RECT, RED, ORANGE


class Bonus:
    WIDTH = 32
    BORDER = 3
    def __init__(self):
        self.reset()
        self.color = WHITE

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        pygame.draw.rect(surface, ORANGE, self.rect, self.BORDER)
        
    def reset(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - self.WIDTH - 20), B_RECT.top + self.WIDTH, self.WIDTH, self.WIDTH)
        self.velx = 2
        self.vely = 2
        self.visible = True
        self.count = 0

    def update(self, surface, ball, game):
        if self.visible:
            self.draw(surface)
            self.rect.x += self.velx
            self.rect.y += self.vely
            if self.rect.left < B_RECT.left or self.rect.right > B_RECT.right:
                self.velx *= -1

            self.getHit(ball)
        else:
            if self.count == 0:
                self.usePower(game)
                self.count += 1

    def getHit(self, ball):
        if self.rect.colliderect(ball.rect):
            self.visible = False

    def usePower(self, game):
        game.lives += 1

class Life(Bonus):
    def __init__(self):
        super().__init__()

    def update(self, surface, ball, game):
        super().update(surface, ball, game)
        if self.visible:
            pygame.draw.circle(surface, RED, (self.rect.centerx, self.rect.centery), self.WIDTH // 3)

    def usePower(self, game):
        game.lives += 1

class AllBonuses:
    def __init__(self):
        self.bonuses = []
        for i in range(10):
            self.bonuses.append(Life())

    def update(self, surface, ball, game, levelNum):
        for index, bonus in enumerate(self.bonuses):
            if index + 1 == levelNum:
                bonus.update(surface, ball, game)

            if bonus.rect.top > HEIGHT:
                bonus.reset()

