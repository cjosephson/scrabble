import board
import agent
import copy
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-m", "--human", action="store_true", dest="human", default=True,
                  help="puts game into AI vs human mode, so you'll be told your tiles")

parser.add_option("-s", "--specify", action="store_true", dest="specify", default=False,
                  help="Specify tiles for the AI")

parser.add_option("-b", "--boss", action="store_true", dest="boss", default=False,
                  help="Boss mode, doesn't check for valid words")
 
(options, args) = parser.parse_args()

def main():
    b = board.Board()
    AI = agent.Agent(b, montecarlo=True)
    scoreOpp = 0
    scoreMe = 0
    tiles = [b.bag.getLetter() for i in xrange(7)]
    #print b
    turn = False
    while True:
        if turn: #AI's turn
            print "Generating AI move..."
            move = AI.move()
            if move != None:
                (word, pos , orientation, usedTiles, score) = move
                if len(word) > 0:
                    row,col = pos
                    scoreMe += score
                    print "Done! AI playing %s at (%s,%s) with score %s."%(word, row, col, score)
                else:
                    print "Done! AI exchanged tiles."
            else:
                print "AI passing turn."
            turn = not turn
        else: #human goes
            valid = False
            while not valid:
                print b
                if options.human: print "Your turn! Tiles:",tiles
                userInput = raw_input("Enter \"word (row,col) 'h'||'v'\": ")
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
                    print "Invalid input format, try again!"
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
                
                orientation = inputList[2].lower()
                if orientation != 'v' and orientation != 'h':
                    print "invalid orientation:",orientation
                    continue
                valid = True
                #if not sure, break out of if
                if options.boss or valid:
                    #make a copy of board and insert to preview move
                    b2 = copy.deepcopy(b)
                    score = b2.insertWord(word, loc, orientation, debug = True)
                    print b2
                    print "Move Score =", score
                    ok = False
                    while not ok:
                        userInput = raw_input("Is this ok? (Y/N) ")
                        valid = b.humanValid(word, loc, orientation, tiles)
                        if ((userInput == "Y" or userInput == "y") and valid):
                            ok=True
                            score = b.insertWord(word, loc, orientation, debug = options.boss)
                            print "move successful"
                            #TODO: fix this?
                            #does not account for the case where a letter on
                            #the board also appears in the tile
                            #set... eit. We'll mostly be doing AI vs AI anyway
                            if options.human:
                                r = 0
                                for l in word:
                                    if l in tiles:
                                        tiles.remove(l)
                                        r += 1
                                for i in xrange(r):
                                    if len(b.bag.letters) > 0:
                                        tiles.append(b.bag.getLetter())
                                    
                            scoreOpp += score
                            valid = True
                            turn = not turn
                        elif (userInput == "N" or userInput == "n"):
                            print "Try Again"
                            break
                        else: 
                            print "Invalid input, try again"
                            break
                else:
                    print "Invalid word!"
            
        print "AI: %s, You: %s, Remaining Tiles: %s"% (scoreMe, scoreOpp, len(b.bag.letters))

main()
