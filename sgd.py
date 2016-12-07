import board
import agent
import copy
import os
from collections import defaultdict 
from util import *

letterMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
             0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O'}

def SGD(eta=1, numIters = 10):
    weights = defaultdict(float)#{}  # feature => weight
    while numIters > 0:
        b = board.Board()
        b.insertWord("UNIVERSITY", (7,3), 'h', debug=True)
        A = agent.Agent(b) #souped up agent
        B = agent.Agent(b) #vanilla agent
        scoreA = 0
        scoreB = 0
        tiles = [b.bag.getLetter() for i in xrange(7)]
        turn = False
        for i in xrange(50):
            if turn: #A's turn
                print "A",
                move = A.move()
                if move != None:
                    (word, (row,col) , orientation, usedTiles, score) = move
                    scoreA += score
                    #print "Done! AI playing %s at (%s,%s) with score %s."%(word, row, col, score)
                turn = not turn
            else:
                print "B",
                move = B.move()
                if move != None:
                    #(word, (row,col) , orientation, usedTiles, score) = move
                    scoreB += move[4]
                    #print "Done! AI playing %s at (%s,%s) with score %s."%(word, row, col, score)
                turn = not turn
        print "scoreA-scoreB",scoreA-scoreB
        numIters -= 1
        '''
        phi_x = featureExtractor()
        # loss_abs = |w*phi(x) - y|
        # grad(loss_abs) = -phi(x)*sgn(y-w*phi(x))
        def grad(phi_x, y, w):
            g = defaultdict(float)
            sign = (1 if y*dotProduct(weights,phi_x) > 0 else -1)
            for k,v in phi_x.iteritems():
                g[k] = -v*sign
                #print "margin, g: %s, %s "%(margin, g)
            return g
        #print "weightsBefore: ",weights
        
        # DESCEND: w = w - eta*grad(loss(x, y w))
        increment(weights, -1*eta, grad(phi_x, y, weights))
        '''
    return weights

def featureExtractor(self, origRack):
    features = {}
    rack = copy.deepcopy(origRack)  
    # Features TODO:
    # -doubles/triples (done)
    # -'qu' (done)
    # -consonants to vowels ratio
    # -include scrabble letter value somehow? sum of tile values
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
            
SGD(numIters = 10)
