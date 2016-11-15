from brain import AJAlgorithm
import board

class Agent:
    def __init__(self, board):
        self.board = Board.board()
        self.brain = AJAlgorithm(self.board)
        self.tiles = []
        
    def move(self):
        pass
