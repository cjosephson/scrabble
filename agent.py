'''The agent runs the AJ algorithm, which generates a list of moves. The
agent chooses the maximal scoring move and plays it on the board

'''
from brain import AJAlgorithm
import board


class Agent:
    def __init__(self, board, debug=False):
        self.board = Board.board()
        self.brain = AJAlgorithm(self.board)
        if debug:
            self.tiles = []
        else:
            self.tiles.append((self.board.bag.getLetter() for i in xrange(7)))
        
    def move(self):

        moves =  brain.generateMoves(tiles)
        #filter any moves that use no letters from the rack
        #(word, score, loc, orientation, usedTiles) = max(moves)
        #print "score of word",self.board.insertWord(word, loc, orientation)
        #(self.tiles.remove(t) for t in usedTiles)
        #(self.tiles.append(self.board.bag.getLetter()) for t in subset)
        #return score
        pass
