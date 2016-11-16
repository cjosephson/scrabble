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
        # compute anchors and crosschecks
        anchors = self.brain.findAnchors()
        h = {}
        v = {}
        for (r,c) in anchors:
            if r not in h:
                h[r] = True
            if c not in v:
                v[c] = True
        for r in h.iterkeys():
            alg.crosschecks(r,'h')
        for c in v.iterkeys():
            alg.crosschecks(c, 'v')

        moves =  brain.generateMoves(tiles)
        #(word, score, loc, orientation, usedTiles) = max(moves)
        #print "score of word",self.board.insertWord(word, loc, orientation)
        #(self.tiles.remove(t) for t in usedTiles)
        #(self.tiles.append(self.board.bag.getLetter()) for t in subset)
        #return score
        pass
