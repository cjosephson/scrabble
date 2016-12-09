'''The agent runs the AJ algorithm, which generates a list of
moves. The agent chooses the maximal scoring move and plays it on the
board

'''
from brain import AJalgorithm
import brain
import copy
import brain as smarts
import board
from operator import itemgetter
from util import * 
from random import shuffle

class Agent:
    def __init__(self, board, debug=False, heuristic=None, montecarlo=False, quackle = False, N=3):
        self.board = board
        self.brain = AJalgorithm(self.board)
        self.tiles = []
        self.debug = debug
        self.heuristic = heuristic
        self.weights = heuristic
        self.montecarlo = montecarlo
        self.quackle = quackle
        self.N = N
        if not debug and len(self.board.bag.letters) > 0:
            self.tiles += [self.board.bag.getLetter() for i in xrange(7)]
        
    def move(self, tiles = None, weights = None):
        if self.heuristic: weights = self.weights
        if not tiles: tiles = self.tiles
        #print "cs221 move with rack",tiles
        self.brain.generateMoves(tiles)
        #print self.board
        #print "There are",len(self.brain.LegalMoves),"legal moves:",#self.brain.LegalMoves
        #for m in self.brain.LegalMoves:
            #print m
        score = 0
        if len(self.brain.LegalMoves) == 0:
            #try tile swap
            if len(self.board.bag.letters) > 0 and len(self.tiles) > 0:
                shuffle(self.tiles)
                discard = self.tiles.pop()
                if not self.quackle: #quackle handles exhanges in quacklemode
                    self.tiles.append(self.board.bag.exchange(discard))
                return ('', discard, None, None, 0)
            return None
        
        moves = sorted(list(self.brain.LegalMoves), key=itemgetter(4), reverse=True)
        #print "moves",moves
        (word, loc, orientation, usedTiles, score) = moves[0] #the top scoring move
        
        #run depth 2 monte carlo on top N=3, returns score
        #difference between agent and simulated opponnent
        if self.montecarlo:
            #print "tiles ++++++++++++++++++",self.tiles
            consider = moves[0:self.N]
            #print "consider",consider
            for i,move in enumerate(consider):
                #print move
                (word, loc, orientation, usedTiles, score) = move
                rack1 = [x for x in self.tiles if x not in usedTiles]
                scoreDiff = brain.runSimulations(rack1, word, loc, orientation, self.board, self.brain, 2)
                #print word, scoreDiff, score
                consider[i] = (scoreDiff, move)
            #print "consider",consider
            (word, loc, orientation, usedTiles, score) = max(consider, key=itemgetter(0))[1] #the top scoring move
            #print "max",max(consider, key=itemgetter(0)) 
            #pass
            
        #run feature extrator on the racks, and also add monte carlo score diff as a feature
        #Do L2 SGD on the feature vector and then select the best one
        if self.heuristic:
            consider = moves[0:self.N]
            for i,move in enumerate(consider):
                (word, loc, orientation, usedTiles, score) = move
                phi = featureExtractor([t for t in self.tiles if t not in usedTiles], score)
                consider[i] = (dotProduct(weights, phi), move)
            #print consider
            (word, loc, orientation, usedTiles, score) = max(consider, key=itemgetter(0))[1] #the top scoring move
            
        #print "max word",word,self.board.insertWord(word, loc, orientation)
        self.board.insertWord(word, loc, orientation)
        #print "usedTiles",usedTiles
        if not self.quackle:
            for t in usedTiles:
                self.tiles.remove(t) 
            #print self.tiles
            for t in usedTiles:
                self.tiles.append(self.board.bag.getLetter())
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
