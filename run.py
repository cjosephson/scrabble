import board
import agent
import copy
from util import *
from random import shuffle
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--boss", action="store_true", dest="boss", default=False,
                  help="Boss mode, doesn't check for valid words")
(options, args) = parser.parse_args()

def main():
    b = board.Board()
    AI = agent.Agent(b)#, montecarlo=True)
    #uncomment to try shorter games
    #shuffle(b.bag.letters)
    #b.bag.letters = b.bag.letters[0:15]
    scoreAI = 0
    scoreHuman = 0
    tiles = [b.bag.getLetter() for i in xrange(7)]
    #print b
    turn = False
    while True:
        if turn: #AI's turn
            if len(AI.tiles) == 0:
                #add opponent tiles to score
                for t in tiles:
                    scoreAI += letterToPoints[t]
                break

            print "Generating AI move..."
            move = AI.move()
            if move != None:
                (word, pos , orientation, usedTiles, score) = move
                if len(word) > 0:
                    row,col = pos
                    scoreAI += score
                    print "Done! AI playing %s at (%s,%s) with score %s."%(word, row, col, score)
                else:
                    print "Done! AI exchanged tiles."
            else:
                print "AI passing turn."
            turn = not turn
        else: #human goes
            if len(tiles) == 0:
                #add opponent tiles to score
                for t in AI.tiles:
                    scoreHuman += letterToPoints[t]
                break
            valid = False
            while not valid:
                print b
                print "Your turn! Tiles:",tiles
                userInput = raw_input("Enter 'word (row,col) h||v', or 'exchange 'c', or 'pass': ")
                inputList = userInput.split()
                if (len(inputList) == 1 and inputList[0] == "pass"):
                    valid = True
                    turn = not turn
                    print "Passing turn."
                    break
                elif (len(inputList) == 2 and inputList[0] == "exchange"):
                    old = inputList[1].upper()
                    print old, tiles
                    if old in tiles and not b.bag.empty():
                        tiles.remove(old)
                        new = b.bag.exchange(old)
                        tiles.append(new)
                        valid = True
                        turn = not turn
                        print "Exchanged tile %s for %s."%(old, new)
                        break
                    else:
                        print "Invalid tile or no tiles in bag!"
                        continue
                elif (len(inputList) != 3):
                    print "****Invalid input format, try again!****"
                    continue
                #parse stuff
                word = inputList[0].upper()
                try:
                    #very dangerous, LOL!
                    loc = eval(inputList[1])
                except:
                    print "could not parse location to tuple format!"
                    continue
                
                if len(loc) != 2:
                    print "invalid (row,col):",loc
                    continue
                elif loc[0]>14 or loc[1]>14 or loc[0]<0 or loc[1]<0:
                    print "rows/cols must be between 0 and 15!"
                    continue
                
                orientation = inputList[2].lower()
                if orientation != 'v' and orientation != 'h':
                    print "invalid orientation:",orientation
                    continue
                valid = True
                #if not sure, break out of if
                if options.boss or valid:
                    #make a copy of board and insert to preview move
                    b2 = copy.deepcopy(b)
                    score = b2.insertWord(word, loc, orientation)
                    b2.insertWord(word,loc,orientation,debug=True)
                    print b2
                    print "Move Score =", score
                    ok = False
                    while not ok:
                        userInput = raw_input("Is this ok? (Y/N) ")
                        validMove = b.humanValid(word, loc, orientation, tiles)
                        if ((userInput == "Y" or userInput == "y") and validMove):
                            ok=True
                            score = b.insertWord(word, loc, orientation, debug = options.boss)
                            print "move successful"
                            r = 0
                            for l in word:
                                if l in tiles:
                                    tiles.remove(l)
                                    r += 1
                            for i in xrange(r):
                                if len(b.bag.letters) > 0:
                                    tiles.append(b.bag.getLetter())
                                    
                            scoreHuman += score
                            valid = True
                            turn = not turn
                        elif (userInput == "N" or userInput == "n"):
                            print "Try Again"
                            break
                        else: 
                            print "****Invalid input, try again****"
                            break
                else:
                    print "Invalid word!"
        print "AI: %s, You: %s, Remaining Tiles: %s"% (scoreAI, scoreHuman, len(b.bag.letters))
    print "Game over!"
main()
