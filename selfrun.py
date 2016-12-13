import board
import agent
import os
from collections import defaultdict 
from util import *

def main(numGames = 1):
    scores = {}
    for i in xrange(numGames):
        b = board.Board()
        #TODO: random seed word?
        seed = "UNIVERSITY"
        b.insertWord(seed, (7,3), 'h', debug=True)
        for c in seed:
            b.bag.popLetter(c)
        #souped up agent
        A = agent.Agent(b, heuristic=weights)#, montecarlo=True)#
        #vanilla agent
        B = agent.Agent(b) 
        scoreAs = 0
        scoreB = 0
        passA = False
        passB = False
        scoreA = 0
        scoreB = 0
        swapA = False
        swapB = False
        while True:
            print "B",
            rackB = B.tiles
            move = B.move()
            if move != None:
                print "moveB",move
                passB = False
                (word, pos , orientation, usedTilesB, score) = move
                if len(word) > 0:
                    swapB = False
                    b.insertWord(word, pos, orientation)
                    #print b
                    #print "bag",b.bag
                    scoreB += score
                else:
                    print "moveB swap"
                    swapB = True

            else: 
                print "moveB pass"
                passB = True
            print "scoreA: %s, scoreB: %s"%(scoreA,scoreB)
            print "A",
            rackA = A.tiles
            move = A.move()
            if move != None:
                print "moveA",move
                passA = False
                (word, pos , orientation, usedTilesB, score) = move
                if len(word) > 0:
                    swapA = False
                    b.insertWord(word, pos, orientation)
                    #print b
                    #print "bag",b.bag
                    scoreA += score
                else:
                    print "moveA swap"
                    swapA = True
            else:
                print "moveA pass"
                passA = True
            
            #endgame if 2 consecutive passes or tileswaps. Ideally,
            #we'd wait 6 tileswaps but that is kinda a bitch to
            #implement.
            if (passA and passB) or (swapA and swapB):
                break
            print "scoreA: %s, scoreB: %s"%(scoreA,scoreB)
        print "GAME scoreA: %s, scoreB: %s"%(scoreA,scoreB)
        scores[i] = (scoreA, scoreB)
        print scores
    return scores

print main(100)
