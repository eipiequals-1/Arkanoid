import pygame

from .constants import WHITE, WIDTH

class Button:
    def __init__(self, color, x, y, w, h, text=""):
        self.color = color
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, surface, size=50, outline=None, font="uroob", fontColor=WHITE):
        border = 4
        if outline:
            pygame.draw.rect(surface, outline, (self.rect.x - border, self.rect.y - border, self.rect.width + border * 2, self.rect.height + border * 2))

        pygame.draw.rect(surface, self.color, self.rect)
        if self.text != "":
            font = pygame.font.SysFont(font, size)
            writing = font.render(self.text, 1, fontColor)
            surface.blit(writing, (self.rect.centerx - writing.get_width() // 2, self.rect.centery - writing.get_height() // 2))

    def isOver(self, pos):
        return self.rect.collidepoint(pos)

class HighScore:
    @staticmethod
    def getMax():
        file = open("highScore.txt", "r")
        f = file.readlines()
        newList = []
        for line in f:
            newList.append(int(line.strip()))

        return max(newList)
        file.close()

    @staticmethod
    def write(text):
        file = open("highScore.txt", "a")
        file.write(text + "\n")

        file.close()
        
def displayText(surface, x, y, text, fontName="uroob", size=35, color=WHITE, centered=True):
    font = pygame.font.SysFont(fontName, size)
    writing = font.render(text, 1, color)
    if not centered:
        surface.blit(writing, (x, y))
    else:
        surface.blit(writing, (WIDTH // 2 - writing.get_width() // 2, y))