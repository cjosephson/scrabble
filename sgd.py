import board
import agent
import os
from collections import defaultdict 
from util import *

letterMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
             0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O'}

def SGD(eta=1, numIters = 10):
    weights = defaultdict(float)#{}  # feature => weight
    weights['raw_score'] = 1 #initialize to all score
    while numIters > 0:
        b = board.Board()
        #TODO: random seed word?
        b.insertWord("UNIVERSITY", (7,3), 'h', debug=True)
        A = agent.Agent(b, heuristic=True) #souped up agent
        B = agent.Agent(b) #vanilla agent
        totA = 0
        totB = 0
        passCount = 0
        for i in xrange(50):
            scoreA = 0
            scoreB = 0
            usedTiles = []
            print "A",
            rack = A.tiles
            print "rack",rack
            move = A.move(weights = weights)
            if move != None:
                (word, (row,col) , orientation, usedTiles, scoreA) = move
                totA += scoreA
            else: 
                if passCount > 2:
                    break #endgame
                passCount += 1
            print "B",
            move = B.move()
            if move != None:
                scoreB = move[4]
                totB += scoreB

            y = scoreA-scoreB
            phi_x = featureExtractor([t for t in rack if t not in usedTiles], scoreA)
            # DESCEND: w = w - eta*grad(loss(x, y w))
            increment(weights, -1*eta, grad(phi_x, y, weights))
            print "scoreA-scoreB",scoreA-scoreB
        numIters -= 1
        print "totA-totB",totA-totB
        print weights
    return weights

# loss_abs = |w*phi(x) - y|
# grad(loss_abs) = -phi(x)*sgn(y-w*phi(x))
def grad(phi_x, y, w):
    g = defaultdict(float)
    sign = (1 if y*dotProduct(w,phi_x) > 0 else -1)
    for k,v in phi_x.iteritems():
        g[k] = -v*sign
    return g
            
SGD(numIters = 10)
