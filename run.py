import board
import baseline
import copy
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-m", "--human", action="store_true", dest="human", default=False,
                  help="puts game into AI vs human mode, so you'll be told your tiles")

(options, args) = parser.parse_args()

def main():
    b = board.Board()
    AI = baseline.Baseline(b)
    scoreOpp = 0
    scoreMe = 0
    if options.human:
        tiles = [b.bag.getLetter() for i in xrange(7)]
    print b
    turn = False
    while True:
        if turn: #AI's turn
            scoreMe += AI.move()
            print b
            turn = not turn
        else: #other goes
            valid = False
            while not valid:
                if options.human: print "Tiles:",tiles
                userInput = raw_input("Enter a word, (row,col) and orientation 'h' or 'v': ")
                inputList = userInput.split()
                if len(inputList) != 3:
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
#b.score
#if not sure, break out of if
                score = b.score(word, loc, orientation)
                print score
                if score > -1:
                   
                    b2 = copy.deepcopy(b)
                    b2.insertWord(word, loc, orientation)
                    print b2
                    print "Move Score= ", score
                    userInput = raw_input("Is this ok? (Y/N) ")   
                    if (userInput == "Y" or userInput == "y"):
                        b.insertWord(word, loc, orientation)
                        print "move successful"
                            #does not account for the case where a letter on
                            #the board also appears in the tile
                            #set... eit. We'll mostly be doing AI vs AI anyway
                        r = 0
                        for l in word:
                            if l in tiles:
                                tiles.remove(l)
                                r += 1
                        for i in xrange(r):
                            tiles.append(b.bag.getLetter())
                    
                        scoreOpp += score
                        print b
                        valid = True
                        turn = not turn
                    elif (userInput == "N" or userInput == "n"):
                        print "Try Again"
                    else: 
                        print "Invalid Input"
                else:
                    print "Invalid word!"
            
        print "AI: %s, Opponent: %s"% (scoreMe, scoreOpp)

main()
