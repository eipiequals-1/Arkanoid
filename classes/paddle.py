import pygame

from .constants import B_RECT, HEIGHT, PADDLE, WIDTH

class Paddle:
    def __init__(self):
        self.reset()

    def draw(self, surface):
        surface.blit(PADDLE, self.rect)

    def update(self, surface, ball, pos):
        self.draw(surface)
        self.useMouse(pos)  
        self.get_hit(ball)

    def useMouse(self, pos):
        if self.rect.left >= B_RECT.left and self.rect.right <= B_RECT.right:
            self.rect.centerx = pos[0]
        if self.rect.left < B_RECT.left:
            self.rect.left = B_RECT.left
        elif self.rect.right > B_RECT.right:
            self.rect.right = B_RECT.right
        
    def get_hit(self, ball):
        diff = ball.rect.centerx - self.rect.centerx
        collisionTolerance = 10
        if self.rect.colliderect(ball.rect):
            if abs(ball.rect.bottom - self.rect.top) < collisionTolerance and ball.vely > 0:
                ball.vely *= -1
                ball.velx = diff // 4

    def reset(self):
        self.rect = PADDLE.get_rect(center=(WIDTH // 2, HEIGHT * 9 // 10))
        self.vel = 0