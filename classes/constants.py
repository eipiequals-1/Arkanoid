import pygame

pygame.init()

WIDTH, HEIGHT = 900, 1200
COLS = 11
BAR_WIDTH = 35

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")
CLOCK = pygame.time.Clock()

# BRICK IMAGES
PADDLE = pygame.transform.scale(pygame.image.load("Assets/platform.png").convert_alpha(), (100, 20))

ARKANOID = pygame.transform.scale(pygame.image.load("Assets/arkanoid_text.png").convert_alpha(), (400, 120))
ARKANOID2 = pygame.transform.scale(pygame.image.load("Assets/arkanoid_text.png").convert_alpha(), (640, 200))

B = []
for i in range(5):
    B.append(pygame.transform.scale(pygame.image.load("Assets/b" + str(i) + ".png").convert_alpha(), (900, 960)))
B_RECT = pygame.Rect((WIDTH//2 - B[0].get_width()//2) + BAR_WIDTH,
                    HEIGHT - B[0].get_height() + BAR_WIDTH,
                    B[0].get_width() - BAR_WIDTH*2,
                    B[0].get_height())

# IMPORTANT BRICK CONSTANTS
CELL_W = B_RECT.width // COLS
CELL_H = 30
START_X = B_RECT.left + (B_RECT.width % COLS) // 2
START_Y = B_RECT.top + 100

# COLORS
RED = (200, 0, 0)
GREEN = (0, 200, 0)
L_BLUE = (0, 231, 249)
F_GREEN = (33, 125, 117)
B_COL = (0, 104, 214)
BLACK = (0, 7, 7)
WHITE = (255, 255, 255)
BLUE = (0, 100, 214)
TAN = (254, 250, 205)
ORANGE = (255, 128, 0)
COLORS = {'R': RED, 'G': GREEN, 'L': L_BLUE, 'T': TAN, 'F': F_GREEN, 'O': ORANGE, 'W': WHITE, 'B': BLUE}
POINTS = {RED: 90, GREEN: 100, L_BLUE: 105, TAN: 210, F_GREEN: 230, ORANGE: 240, WHITE: 150, BLUE: 120}

LEVELS = [
    # Level 1
    ["FFFFFFFFFFF",
     "RRRRRRRRRRR",
     "OOOOOOOOOOO",
     "BBBBBBBBBBB",
     "TTTTTTTTTTT",
     "GGGGGGGGGGG"],
    # Level 2
    ["FFFFFFFFFFF",
     "FFFFFFFFFFF",
     "           ",
     "RO ORRRO OR",
     "RO ORRRO OR",
     "RO ORRRO OR",
     "RO ORRRO OR",
     "           ",
     "WWWWWWWWWWW",
     "WWWWWWWWWWW"],
    # Level 3
    ["TTTTTTTTTTT",
     "           ",
     "R          ",
     "RL         ",
     "RLF        ",
     "RLFG       ",
     "RLFGB      ",
     "RLFGBW     ",
     "RLFGBWO    ",
     "RLFGBWOR   ",
     "RLFGBWORL  ",
     "RLFGBWORLF ",
     "RLFGBWORLFG",
     "           ",
     "LLLLLLLLLLL"],
    # Level 4
    ["OOOOOOOOOOO",
     "   O    OR ",
     " O O    O  ",
     " O O  O O  ",
     " O O  O O  ",
     " O O RO O  ",
     " O O  O O  ",
     " O O  O O  ",
     " O O  O O  ",
     " O O  O O  ",
     " O    O    ",
     " O    O   R",
     " OOOOOOOOOO"],
    # Level 5
    ["LWOLLLLLOWL",
     "LWROLLLORWL",
     "LWRROWORRWL",
     "LWRRRWRRRWL",
     "LWRRRWRRRWL",
     "LWRRRWRRRWL",
     "LGRRRWRRRGL",
     "LLGRRWRRGLL",
     "LLLGRWRGLLL"],
    # Level 6
    ["BBBBBBBBBBB",
     "O         O",
     "           ",
     "OFFFFFFFFFO",
     "O         O",
     "WWWWWWWWWWW",
     "           ",
     "LFFFFFFFFFL",
     "O         O",
     "RRRRRRRRRRR",
     "           ",
     "RRRRRRRRRRR",
     "O         O"],
    # Level 7
    ["OOOOOOOOOOO",
     "O         O",
     "O LLLLLLL O",
     "O L     L O",
     "O L RRR L O",
     "O L RBR L O",
     "O L RFR L O",
     "O L RRR L O",
     "O L     L O",
     "O LLLLLLL O",
     "O         O",
     "OOOOOOOOOOO"],
    # Level 8
    ["LLLLLLLLLLL",
     "           ",
     "GG GG GG GG",
     "GG GG GG GG",
     "           ",
     " LLL LL LLL",
     " LLL LL LLL",
     "           ",
     "RRR RRR RRR",
     "RLR RLR RLR",
     "RRR RRR RRR",
     "           ",
     "LLLLLLLLLLL"],
    # Level 9
    ["RRRRRRRRRRR",
     "GGGGGGGGGGG",
     "BBBBBBBBBBB",
     "OOOOLLLOOOO",
     "ORRO   OBBO",
     "ORRO   OBBO",
     "O         O",
     "O         O",
     "O   OOO   O",
     "O   OOO   O",
     "OLLLOOOLLLO"],
    # Level 10
    ["RB         ",
     "RBLG       ",
     "RBLGTF     ",
     "RBLGTFWO   ",
     "RBLGTFWORG ",
     "RBLGTFWORGL",
     "RBLGTFWORGL",
     "  LGTFWORGL",
     "    TFWORGL",
     "      WORGL",
     "        RGL",
     "          L"]
]