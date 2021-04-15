import sys

import pygame

from .ball import Ball
from .bonus import AllBonuses
from .constants import *
from .GUI import Button, HighScore, displayText
from .level import Level
from .paddle import Paddle

pygame.init()
#music = pygame.mixer.music.load("Assets/")

class Game:
    """
    The main loop where all events and actions are controlled.
    Creates an instance of the necessary ball, paddle, bricks, buttons, scores, etc.
    Separates the game into states where in each state specific updates and events are assigned.
    """
    def __init__(self):
        self.running = True
        self.state = "menu"
        self.levelNum = 1
        self.paddle = Paddle()
        self.ball = Ball(WIDTH // 2 - 25 // 2, self.paddle.rect.top - 25, 25, 25)
        self.level = Level(self.levelNum)
        self.score = 0
        self.lives = 15
        self.createButtons()
        self.highScore = HighScore()
        self.allBonuses = AllBonuses()

    def run(self):
        # game while loop
        while self.running:
            self.update()
            self.events()      
            pygame.display.update()
            CLOCK.tick(60)
            
    def update(self):
        # Checks for collisions, points, wins, and losses
        win = self.level.getWin()
        lose = self.level.getLose(self)
        ###################### PLAYING #########################################
        if self.state.__eq__("playing"):

            pos = pygame.mouse.get_pos()
            SCREEN.fill(BLACK)
            SCREEN.blit(ARKANOID, (WIDTH // 2 - ARKANOID.get_width() // 2, B_RECT.top // 3 - ARKANOID.get_height() // 2))
            SCREEN.blit(B[(self.levelNum - 1) // 2], (B_RECT.x - BAR_WIDTH, B_RECT.y - BAR_WIDTH))
            self.leave.draw(SCREEN, 25)
            self.allBonuses.update(SCREEN, self.ball, self, self.levelNum)
            self.ball.update(SCREEN, WIDTH // 2 - 25 // 2, self.paddle.rect.top - 25, 25, 25, self)
            self.level.update(SCREEN, self.ball, self, self.highScore)
            self.paddle.update(SCREEN, self.ball, pos)
            if win:
                pygame.time.delay(2000)
                self.state = "win"
            elif lose:
                pygame.time.delay(2000)
                self.state = "lose"
                self.lives = 15

        self.menuUpdate()
        self.extrasUpdate()
  
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.highScore.write(str(self.score))
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.state.__eq__("playing"): ########### PLAYING ###########
                    if self.leave.isOver(pos):
                        self.resetLevel(self.levelNum)
                        self.state = "menu"

                elif self.state.__eq__("menu"): ############### MENU ###########
                    if self.start.isOver(pos):
                        self.state = "playing"
                    if self.credits.isOver(pos):
                        self.state = "credits"
                    if self.select.isOver(pos):
                        self.state = "select"
                    if self.settings.isOver(pos):
                        self.state = "settings"

                elif self.state.__eq__("credits"): ########### CREDITS #########
                    if self.leave.isOver(pos):
                        self.resetLevel()
                        self.state = "menu"

                elif self.state.__eq__("win"): ############### WIN #############
                    if self.nextLevel.isOver(pos):
                        if self.levelNum == 10:
                            self.resetLevel(1)
                        else:
                            self.resetLevel()

                        self.state = "playing"

                elif self.state.__eq__("select"): ############ SELECT ##########
                    for index, button in enumerate(self.levels):
                        if button.isOver(pos):
                            self.resetLevel(index + 1)
                            self.state = "playing"
                    if self.leave.isOver(pos):
                        self.resetLevel()
                        self.state = "menu"

                elif self.state.__eq__("settings"): ########## SETTINGS ########
                    if self.leave.isOver(pos):
                        self.resetLevel()
                        self.state = "menu"

                elif self.state.__eq__("lose"): ############# LOSE #############
                    self.resetLevel(1)
                    self.state = "menu"
                    self.score = 0
                    
    def resetLevel(self, chosenLevel=None):
        if chosenLevel is None:
            self.levelNum += 1
            self.level.bricks.clear()
            self.level.initialize(self.levelNum)
            self.highScore.write(str(self.score))
            self.ball.reset(WIDTH // 2 - 25 // 2, self.paddle.rect.top - 25, 25, 25)
            self.paddle.reset()
        else:
            self.levelNum = chosenLevel
            self.level.bricks.clear()
            self.level.initialize(self.levelNum)
            self.highScore.write(str(self.score))
            self.ball.reset(WIDTH // 2 - 25 // 2, self.paddle.rect.top - 25, 25, 25)
            self.paddle.reset()

    def createButtons(self):
        self.start = Button(BLACK, WIDTH // 2 - 50, HEIGHT * 3 // 5, 100, 50, "Start")
        self.nextLevel = Button(BLACK, WIDTH // 2 - 50, HEIGHT * 4 // 5, 100, 30, "Continue")
        self.credits = Button(BLACK, WIDTH // 2 - 50, HEIGHT * 22 // 25, 100, 30, "Credits")
        self.leave = Button(BLACK, WIDTH - 100, HEIGHT * 1 // 200, 90, 30, "Leave")
        self.select = Button(BLACK, WIDTH // 2 - 80, HEIGHT * 17 // 25, 160, 30, "Select Level")
        self.settings = Button(BLACK, WIDTH // 2 - 50, HEIGHT * 18 // 25, 100, 30, "Settings")
        self.levels = []
        self.sEffectsOn = Button(BLACK, WIDTH // 2 - 50, HEIGHT // 2, 100, 40, "Sound Effects: ON")
        self.sEffectsOff = Button(BLACK, WIDTH // 2 - 50, HEIGHT // 2, 100, 40, "Sound Effects: OFF")
        
        buttonW = 80
        columnNo = 5
        spaceBtwn = (WIDTH - (buttonW * columnNo)) // (columnNo + 1)
        for i in range(columnNo):
            self.levels.append(Button(BLACK, spaceBtwn + (buttonW * (i)) + (spaceBtwn * (i)), 200, buttonW, buttonW, str(i + 1)))
        for i in range(columnNo):
            self.levels.append(Button(BLACK, spaceBtwn + (buttonW * (i)) + (spaceBtwn * (i)), 400, buttonW, buttonW, str(i + 1 + columnNo)))

    def menuUpdate(self):
        ############################### MENU ###################################
        if self.state.__eq__("menu"):
            SCREEN.fill(BLACK)
            self.start.draw(SCREEN, 35)
            self.credits.draw(SCREEN, 30)
            self.select.draw(SCREEN, 25)
            self.settings.draw(SCREEN, 25)
            SCREEN.blit(ARKANOID2, (WIDTH // 2 - ARKANOID2.get_width() // 2, HEIGHT // 10))
            
    def extrasUpdate(self):
        ################################### OVER ##############################        
        if self.state.__eq__("win"):
            SCREEN.fill(BLACK)
            displayText(SCREEN, WIDTH // 2, HEIGHT // 2 - 17, "You Win!")
            self.leave.draw(SCREEN, 25)
            #These are the buttons to control levels
            self.nextLevel.draw(SCREEN, 35)
                
        elif self.state.__eq__("lose"):
            SCREEN.fill(BLACK)
            displayText(SCREEN, WIDTH // 2, HEIGHT // 2 - 17, "You Lose!")
            self.leave.draw(SCREEN, 25)

        ################################# CREDITS ##############################
        elif self.state.__eq__("credits"):
            SCREEN.fill(BLACK)
            displayText(SCREEN, WIDTH // 7, HEIGHT * 11 // 25, "Python 3.8.5", "uroob", 30, WHITE, False)
            displayText(SCREEN, WIDTH // 7, HEIGHT * 12 // 25, "Pygame 1.9.6", "uroob", 30, WHITE, False)
            displayText(SCREEN, WIDTH // 7, HEIGHT * 15 // 25, "December 2020", "uroob", 30, WHITE, False)
            displayText(SCREEN, WIDTH // 7, HEIGHT * 7 // 25, "Arkanoid Version 3.7", "uroob", 30, WHITE, False)
            self.leave.draw(SCREEN, 25)

        ############################ SETTINGS ##################################
        elif self.state.__eq__("settings"):
            SCREEN.fill(BLACK)
            self.leave.draw(SCREEN, 25)

        ################################ SELECT ################################
        elif self.state.__eq__("select"):
            SCREEN.fill(BLACK)
            displayText(SCREEN, WIDTH // 2, HEIGHT * 1 // 10, "Select A Level", "uroob", 30, BLUE)
            self.leave.draw(SCREEN, 25)
            for button in self.levels:
                button.draw(SCREEN, 35)
                
    @staticmethod
    def drawGrid():
        for i in range(20):
            pygame.draw.line(SCREEN, (128, 128, 128), (START_X + CELL_W * i, 0), (START_X + CELL_W * i, HEIGHT))
            
        for x in range(20):
            pygame.draw.line(SCREEN, (128, 128, 128), (B_RECT.left, START_Y + CELL_H * x), (B_RECT.right, START_Y + CELL_H * x))