'''The agent runs the AJ algorithm, which generates a list of
moves. The agent chooses the maximal scoring move and plays it on the
board

'''
from brain import AJalgorithm
import board
from operator import itemgetter

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',\
	    'H', 'I', 'J', 'K', 'L', 'M', 'N',\
	    'O', 'P', 'Q', 'R', 'S', 'T', 'U',\
	    'V', 'W', 'X', 'Y', 'Z']

class Agent:
    def __init__(self, board, debug=False, heuristic=False, montecarlo=False, quackle = False, N=3):
        self.board = board
        self.brain = AJalgorithm(self.board)
        self.tiles = []
        self.debug = debug
        self.heuristic = heuristic
        self.montecarlo = montecarlo
        self.quackle = quackle
        self.N = N
        if not debug and len(self.board.bag.letters) > 0:
            self.tiles += [self.board.bag.getLetter() for i in xrange(7)]
        
    def move(self, tiles = None):
        if not tiles: tiles = self.tiles
        #print "AI move with rack",tiles
        self.brain.generateMoves(tiles)
        #print self.board
        #print "There are",len(self.brain.LegalMoves),"legal moves:",self.brain.LegalMoves
        #for m in self.brain.LegalMoves:
            #print m
        score = 0
        if len(self.brain.LegalMoves) == 0:
            return None
        
        moves = sorted(list(self.brain.LegalMoves), key=itemgetter(4), reverse=True)
        #print "moves",moves
        (word, loc, orientation, usedTiles, score) = moves[0] #the top scoring move
        
        #run depth 2 monte carlo on top N=3, returns score
        #difference between agent and simulated opponnent
        if self.montecarlo:
            pass
            
        #run feature extrator on the racks, and also add monte carlo score diff as a feature
        #Do L2 SGD on the feature vector and then select the best one
        w = {}
        if self.heuristic:
            consider = moves[0:self.N]
            for i,move in enumerate(consider):
                (word, loc, orientation, usedTiles, score) = move
                phi = self.rackFeatureExtractor(usedTiles)
                consider[i] = (dotProduct(weights, featureExtractor(x)), m)
            (word, loc, orientation, usedTiles, score) = max(consider, key=itemgetter[0]) #the top scoring move
            
        #print "max word",word,self.board.insertWord(word, loc, orientation)
        self.board.insertWord(word, loc, orientation)
        #print "usedTiles",usedTiles
        if not self.quackle:
            for t in usedTiles:
                self.tiles.remove(t) 
            #print self.tiles
            for t in usedTiles:
                self.tiles.append(self.board.bag.getLetter())
            #print self.tiles
        return (word, loc, orientation, usedTiles, score)

    #TODO: merge this with normal move, just add a quackle mode to move
    def quackleMove(self, tiles):
        if not tiles: tiles = self.tiles
        self.brain.generateMoves(tiles)
        if len(self.brain.LegalMoves) > 0:
            (word, loc, orientation, usedTiles, score) = max(self.brain.LegalMoves, key=itemgetter(4))
            self.board.insertWord(word, loc, orientation)
            return (word, loc, orientation, usedTiles, score)
        else: 
            return None
        
    def rackFeatureExtractor(self, origRack):
        features = {}
        rack = copy.deepcopy(origRack)  
        #even to odd ratop
        #features['rato'] = 
        if ('Q' in rack) and ('U' in rack): features['QU'] = 1

        for char in alphabet:
            c2 = char+char
            c3 = char+char+char
            if char in rack:
                rack.remove(char)
                if char in rack:
                    rack.remove(char)
                    if (char) in rack: 
                        features[c2] = 1
                    else:
                        features[c3] = 1
                else:
                    features[char] = 1
        return features

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
