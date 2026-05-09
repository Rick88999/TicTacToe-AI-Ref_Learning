import pygame
import numpy as np
import json

class AI_system:
    def __init__(self):
        self.mosse = []
        with open("AIData.json", "r") as f:
            self.AIData = json.load(f)
    
    def respondeMove(self, board):
        i = 0
        shadow_board = np.array([])
        for rows in board:
            for box in rows:
                if(box.symbol == "X"):
                    shadow_board = np.append(shadow_board, "X")
                elif(box.symbol == "O"):
                    shadow_board = np.append(shadow_board, "O")
                else:
                    shadow_board = np.append(shadow_board, " ")

        shadow_board = shadow_board.reshape(3, 3)

        for id, table in self.AIData.items():
            if(np.array_equal(table[0], shadow_board)):
                moves = np.array(table[1])
                i, j = np.unravel_index(np.argmax(moves), moves.shape)
                self.mosse.append((id, i, j))
                return i, j
            
        return None
    
    def setNewData(self, result):
        if(result == "win"):
            for id, i, j in self.mosse:
                print(f"Aggiornando la mossa per l'ID {id}: ({i}, {j}) con value=> {self.AIData[id][1][i][j]} a value=> {self.AIData[id][1][i][j] + 0.1}")
                self.AIData[id][1][i][j] += 0.1
        elif(result == "lose"):
            for id, i, j in self.mosse:
                print(f"Aggiornando la mossa per l'ID {id}: ({i}, {j}) con value=> {self.AIData[id][1][i][j]} a value=> {self.AIData[id][1][i][j] - 0.2}")
                self.AIData[id][1][i][j] -= 0.2
        elif(result == "draw"):
            for id, i, j in self.mosse:
                print(f"Aggiornando la mossa per l'ID {id}: ({i}, {j}) con value=> {self.AIData[id][1][i][j]} a value=> {self.AIData[id][1][i][j] + 0.05}")
                self.AIData[id][1][i][j] += 0.05
        
        with open("AIData.json", "w") as f:
            json.dump(self.AIData, f)
        print("AIData aggiornato con risultato:", result)



        
        