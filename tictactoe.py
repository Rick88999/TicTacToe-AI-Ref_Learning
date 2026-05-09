import pygame
import numpy as np
import sys
import CPUVersus
import time

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

def check_winner(board):
    winner = None
    counter = 0
    
    for i in range(3):
        if board[i][0].symbol == board[i][1].symbol == board[i][2].symbol != None:
            winner = board[i][0].symbol
        if board[0][i].symbol == board[1][i].symbol == board[2][i].symbol != None:
            winner = board[0][i].symbol

    if board[0][0].symbol == board[1][1].symbol == board[2][2].symbol != None:
        winner = board[0][0].symbol
    if board[0][2].symbol == board[1][1].symbol == board[2][0].symbol != None:
        winner = board[0][2].symbol

    for i in range(3):
        for j in range(3):
            if board[i][j].symbol != None:
                counter += 1
    if counter == 9 and winner == None:
        return "draw"
    
    return winner

def show_winner(winner):
    if winner == "X":
        AI_system.setNewData("lose")
        time.sleep(2)
        pygame.quit()
    elif winner == "O":
        AI_system.setNewData("win")
        time.sleep(2)
        pygame.quit()
    elif winner == "draw":
        AI_system.setNewData("draw")
        time.sleep(2)
        pygame.quit()
    
    
class game:
    def __init__(self):
        self.board = self.initBoard()  
        self.turn = 1
    
    def getBoard(self):
        return self.board

    def initBoard(self):
        collBox = np.array([])  # Array per le hitbox

        for i in range(3):
            for j in range(3):
                collBox = np.append(collBox, hitbox(j, i))

        return collBox.reshape(3, 3)

    def changeTurn(self):
        if(self.turn == 0):
            self.turn = 1
        else:            
            self.turn = 0

class hitbox:
    def __init__(self, x, y):
        self.box = pygame.Rect(x*BASEHITBOX, y*BASEHITBOX, BASEHITBOX, BASEHITBOX)
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
AI_system = CPUVersus.AI_system()

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
            show_winner(check_winner(gameManager.getBoard()))
            AI_responde = AI_system.respondeMove(gameManager.getBoard())
            if AI_responde is not None:
                i, j = AI_responde
                box = gameManager.getBoard()[i][j]
                box.symbol = 'O'
                box.drawO()
                gameManager.changeTurn()
            else:
                print("AI non ha trovato una mossa valida.")
            show_winner(check_winner(gameManager.getBoard()))

            
            
            
            

    pygame.display.update()