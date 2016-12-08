import board
import agent
import copy
import os
from util import *
from random import randint
from time import sleep
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-n", "--numgames", action="store", type="int", dest="numgames", default=1,
                  help="how many games to autoplay")
parser.add_option("-p", "--prefix", action="store", type="string", dest="path", 
                  default="/home/cjoseph/Documents/quackle/test", help="path prefix for quackgame and cs221game files")
parser.add_option("-s", "--silent", action="store_true", dest="silent", default=False, 
                  help="non-verbose mode only outputs game scores and a summary")
(options, args) = parser.parse_args()

letterMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
             0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O'}
scores = {}

def main():
    #delete old game files
    i = 0
    while True:
        try:
            os.remove(options.path+"/quackgame-%i.gcg"%i)
            os.remove(options.path+"/cs221game-%i"%i)
            i += 1
        except OSError:
            break

    #start quackle game in background
    print "starting quackle..."
    os.system("cd "+options.path+" && ./test  --repetitions=%i lexicon=cs221 --mode=cs221 --quiet &"%options.numgames)
    sleep(1)
    print "done."
    
    for i in xrange(0, options.numgames):    
        sleep(1)
        you = open(options.path+"/quackgame-%i.gcg"%i,'r')
        me = open(options.path+"/cs221game-%i"%i,'w+')

        b = board.Board()
        AI = agent.Agent(b, quackle=True)
        scoreYou = 0
        scoreMe = 0
        if not options.silent: print b
        OK  = True
        yourMove = ""
        myMove = ""
        print "-------------------------------------------------"
        print "playing game %i of %i"%(i+1, options.numgames)
        print "-------------------------------------------------"

        while True:
            y = you.readline().strip()
            #m = me.readline().strip()
            if y != yourMove and y != "":
                yourMove = y.split()
                #print "yourMove",yourMove
                player = yourMove[0]
                if player == "quackle":
                    if not options.silent: print "quackle move",yourMove
                    else: print "q",
                    orientation= yourMove[1]
                    loc = (int(yourMove[2]), int(yourMove[3]))
                    if len(yourMove) == 5:
                        word = yourMove[4].upper()
                        if not options.silent: print "word, loc, score:",word,loc,orientation,scoreYou
                        scoreYou += b.insertWord(word, loc, orientation, debug = False)
                    elif len(yourMove) > 5: #abort
                        print yourMove
                        print "breaking"
                        break
                    else:
                        if not options.silent: print "quackle pass?"
                    
                elif player == "cs221":
                    rack = yourMove[-1]
                    #wildcard tiles, add a vowel if we have none
                    #otherwise pick a random letter
                    wildcard = ''
                    if sum([1 for v in vowels if v in rack]) > 0:
                        wildcard = vowels[randint(0,5)]
                    else:
                        wildcard = alphabet[randint(0,25)]
                    rack.replace('?',wildcard)
                    move = AI.move([t for t in rack])
                    if not options.silent: print "cs221 move",move
                    else: print "c",
                    if move != None: #write move to file
                        (word, pos , orientation, usedTiles, score) = move
                        if len(word) > 0:
                            row,col = pos
                            scoreMe += score
                            if wildcard in usedTiles:
                                word = list(word)
                                word[word.index(wildcard)]=wildcard.upper()
                                word = ''.join(word)
                            me.write("%s %s %s %s %s\n"%(word,
                                                         row,
                                                         col,
                                                         orientation,
                                                         score))
                            me.flush()
                        else: #tile exchange
                            tile = pos
                            me.write("%s %s\n"%("exchange", tile))
                            me.flush()
                    else: #write pass to file
                        me.write("pass\n")
                        me.flush()
                elif player == "Game": #game over
                    print "Game over!"
                    break
                else: #TODO: this shouldn't happen, fix it!
                    print "file %s in a bad state, ending"%you
                    me.write("end\n")
                    me.flush()
                    OK = False
                    break
                if not options.silent: 
                    print b
                    print "CS221: %s, Quackle: %s"% (scoreMe, scoreYou)
        if OK:
            print "Game score CS221: %s, Quackle: %s"% (scoreMe, scoreYou)
            scores[i]=(scoreMe,scoreYou)
        else: #don't add score for terminated games
            OK = True
        #print "scores (cs221, quackle):",scores
    print "scores (cs221, quackle):",scores
main()
