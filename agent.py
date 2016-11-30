'''The agent runs the AJ algorithm, which generates a list of moves. The
agent chooses the maximal scoring move and plays it on the board

'''
from brain import AJalgorithm
import board
from operator import itemgetter

class Agent:
    def __init__(self, board, debug=False):
        self.board = board
        self.brain = AJalgorithm(self.board)
        self.tiles = []
        if not debug:
            self.tiles += [self.board.bag.getLetter() for i in xrange(7)]
        
    def move(self, tiles = None):
        if not tiles: tiles = self.tiles
        moves =  self.brain.generateMoves(tiles)
        print self.board
        print "There are",len(self.brain.LegalMoves),"legal moves:",self.brain.LegalMoves
        #for m in self.brain.LegalMoves:
            #print m
        score = 0
        if len(self.brain.LegalMoves > 0):
            (word, loc, orientation, usedTiles, score) = max(self.brain.LegalMoves, key=itemgetter(4))
            print "max word",word,self.board.insertWord(word, loc, orientation)
            self.board.insertWord(word, loc, orientation)
        #(self.tiles.remove(t) for t in usedTiles)
        #(self.tiles.append(self.board.bag.getLetter()) for t in subset)
        return score

    def quackleMove(self, tiles):
        if not tiles: tiles = self.tiles
        moves =  self.brain.generateMoves(tiles)
        (word, loc, orientation, usedTiles, score) = max(self.brain.LegalMoves, key=itemgetter(4))
        self.board.insertWord(word, loc, orientation)
        return (word, loc, orientation, usedTiles, score)


if __name__ == "__main__":
    b = board.Board()
    a = Agent(b)
    #b.insertWord("UNIVERSITY", (7,3), 'h', debug=True) 
    #b.insertWord("AH", (4,4), 'v', debug=True)
    b.insertWord("SKATE", (7,7), 'h')
    b.insertWord("WET", (5,10), 'v')
    b.insertWord("SUN", (3,5), 'h')
    a.move()
    print b
