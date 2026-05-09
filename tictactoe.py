import pygame
import numpy as np
import sys

BASEHITBOX = 100
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BG_COLOR = (0, 0, 0)
LINE_COLOR = (180, 100, 255)

pygame.init()

def initScreen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    pygame.display.set_caption("Tic Tac Toe")
    return screen

def draw_lines():
    # Disegna 2 linee orizzontali e 2 verticali
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)

class game:
    def __init__(self):
        self.board = self.initBoard()  
        self.turn = 0
    
    def getBoard(self):
        return self.board

    def initBoard(self):
        collBox = np.array([])  # Array per le hitbox

        for i in range(3):
            for j in range(3):
                collBox = np.append(collBox, hitbox(j*BASEHITBOX, i*BASEHITBOX, BASEHITBOX, BASEHITBOX))

        return collBox.reshape(3, 3)

    def changeTurn(self):
        if(self.turn == 0):
            self.turn = 1
        else:            
            self.turn = 0

class hitbox:
    def __init__(self, x, y, width, height):
        self.box = pygame.Rect(x, y, width, height)
        self.symbol = None  # 'X' o 'O'

    def collidepoint(self, pos):
        return self.box.collidepoint(pos)
    
    def drawX(self):
        
        offset = 20
        
        
        start_1 = (self.box.left + offset, self.box.top + offset)
        end_1 = (self.box.right - offset, self.box.bottom - offset)

        start_2 = (self.box.right - offset, self.box.top + offset)
        end_2 = (self.box.left + offset, self.box.bottom - offset)
        
        pygame.draw.line(screen, (3, 71, 232), start_1, end_1, 10)
        pygame.draw.line(screen, (3, 71, 232), start_2, end_2, 10)

        pygame.display.flip()

    def drawO(self):
        center = self.box.center
        radius = self.box.width // 2 - 20
        pygame.draw.circle(screen, (255, 0, 0), center, radius, 10)
        pygame.display.flip()



gameManager = game()

screen=initScreen()
draw_lines()

# Loop principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = event.pos
            print(pos)

            for row in gameManager.getBoard():
                for box in row:
                    if box.collidepoint(pos):
                        if box.symbol is None and gameManager.turn == 1:
                            box.symbol = 'X'
                            box.drawX()
                            gameManager.changeTurn()
                        elif box.symbol is None and gameManager.turn == 0:
                            box.symbol = 'O'
                            box.drawO()
                            gameManager.changeTurn()
    
    
    pygame.display.update()