import board
import agent
import os
from collections import defaultdict 
from util import *

letterMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
             0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O'}

def SGD(numIters, eta=1):
    log = []
    weights = defaultdict(float)#{}  # feature => weight
    weights['raw_score'] = 1 #initialize to all score
    while numIters > 0:
        b = board.Board()
        ys = [] 
        #TODO: random seed word?
        seed = "UNIVERSITY"
        b.insertWord(seed, (7,3), 'h', debug=True)
        for c in seed:
            b.bag.popLetter(c)
        
        A = agent.Agent(b, heuristic=weights, montecarlo=True) #souped up agent
        B = agent.Agent(b) #vanilla agent
        totA = 0
        totB = 0
        for i in xrange(50):
            scoreA = 0
            scoreB = 0
            usedTilesA = []
            usedTilesB = []
            #print "A",
            rackA = A.tiles
            move = A.move(weights = weights)
            if move != None:
                (word, pos , orientation, usedTilesA, scoreA) = move
                if len(word) > 0:
                    #print "moveA",move
                    b.insertWord(word, pos, orientation)
                    totA += scoreA
            #print "A mc_score = ",A.mc_score,"A score=",scoreA
            #print "B",
            rackB = B.tiles
            move = B.move()
            if move != None:
                (word, pos, orientation, usedTilesB, scoreB) = move
                if len(word) > 0:
                    #print "moveA",move
                    b.insertWord(word, pos, orientation)
                    #print "moveB",move
                    totB += scoreB

            y = scoreA-scoreB
            ys.append(y)
            #if scores haven't changed for 3 rounds, game over
            #print "ys",ys[-3:]
            if len(ys) > 3 and len(set(ys[-3:])) == 1:
                print "endgame"
                break #endgame

            phi_A = featureExtractor([t for t in rackA if t not in usedTilesA],
                                     scoreA, mc_score = A.mc_score)
            phi_B = featureExtractor([t for t in rackB if t not in usedTilesB], scoreB)
            #print "phi_A",phi_A
            #print "phi_B",phi_B
            # ASCEND: w = w + eta*grad(w*phi(A) - w*phi(B))*y
            # loss = w*phi(A) - w*phi(B)
            # grad(loss) = phi(A)-phi(B)
            grad = copy.deepcopy(phi_A); increment(grad, -1, phi_B)
            increment(weights, eta*y, grad)
            print "scoreA-scoreB",scoreA-scoreB
        numIters -= 1
        print "%s iters remaining, totA-totB: %s"%(numIters,totA-totB)
        print "weights",weights
        log.append(totA-totB)

    print log
    return weights

print SGD(numIters = 50)

