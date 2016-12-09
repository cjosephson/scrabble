import board
import agent
import os
from collections import defaultdict 
from util import *

def main(numGames = 1):
    scores = {}
    weights = {'A': 142, 'AAA': 94, 'BB': 16, 'EEE': 29, 'L': 204, 'NNN': -59, 'RR': 12, 'TT': 24, 'TTT': 43, 'EE': -327, 'GGG': 8, 'III': 66, 'RRR': 20, 'AA': 163, 'C': 89, 'B': 68, 'E': 225, 'D': 130, 'G': -35, 'F': 29, 'I': 17, 'H': 32, 'K': -50, 'J': 35, 'M': -22, 'vc_ratio': -1077.6666666666665, 'O': 41, 'N': 81, 'Q': -279, 'P': 48, 'S': 60, 'R': 95, 'raw_score': 24565, 'T': 148, 'W': 269, 'V': -22, 'Y': 35, 'X': 3, 'Z': -39, 'OO': 22, 'II': -204, 'WWW': 19, 'QU': -194, 'UUU': -200, 'OOO': -15, 'YYY': 10, 'SSS': 18, 'SS': -10, 'U': 103, 'BBB': 6}
    for i in xrange(numGames):
        b = board.Board()
        #TODO: random seed word?
        b.insertWord("UNIVERSITY", (7,3), 'h', debug=True)
        A = agent.Agent(b, heuristic=weights) #souped up agent
        B = agent.Agent(b) #vanilla agent
        scoreAs = 0
        scoreB = 0
        passA = False
        passB = False
        scoreA = 0
        scoreB = 0
        swapA = False
        swapB = False
        while True:
            print "A",
            rackA = A.tiles
            move = A.move()
            if move != None:
                print "moveA",move
                passA = False
                (word, pos , orientation, usedTilesA, score) = move
                if len(word) > 0:
                    swapA = False
                    b.insertWord(word, pos, orientation)
                    print b
                    scoreA += score
                else:
                    swapA = True

            else: 
                passA = True
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
                    print b
                    scoreB += score
                else:
                    swapB = True
            else:
                passB = True
                
            #endgame if 2 consecutive passes or tileswaps. Ideally,
            #we'd wait 6 tileswaps but that is kinda a bitch to
            #implement.
            if (passA and passB) or (swapA and swapB):
                break
        print "scoreA: %s, scoreB: %s"%(scoreA,scoreB)
        scores[i] = (scoreA, scoreB)
    return scores

print main(10)
