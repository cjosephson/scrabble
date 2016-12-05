import board
import agent
import copy
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-m", "--human", action="store_true", dest="human", default=False,
                  help="puts game into AI vs human mode, so you'll be told your tiles")

parser.add_option("-s", "--specify", action="store_true", dest="specify", default=False,
                  help="Specify tiles for the AI")

parser.add_option("-b", "--boss", action="store_true", dest="boss", default=False,
                  help="Boss mode, doesn't check for valid words")

(options, args) = parser.parse_args()

def main():
    b = board.Board()
    AI = agent.Agent(b)
    scoreOpp = 0
    scoreMe = 0
    if options.human:
        tiles = [b.bag.getLetter() for i in xrange(7)]
    print b
    turn = False
    while True:
        if turn: #AI's turn
            if options.specify:
                while True:
                    userInput = raw_input("Enter 7 tiles for AI (e.g. ABCDEF): ")
                    if len(userInput) != 7:
                        print "Not seven letters!"
                    elif not userInput.isalpha():
                        print "Must be letters!"
                    else:
                        AItiles=[i for i in userInput.upper()]
                        break
           
                scoreMe += AI.move(AItiles) 
            else: AItiles = None
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
                print "checking score"
                score = b.score(word, loc, orientation)
                print score
                if options.boss or score > -1:
                    #make a copy of board and insert to preview move
                    b2 = copy.deepcopy(b)
                    b2.insertWord(word, loc, orientation, debug = options.boss)
                    print b2
                    print "Move Score= ", score
                    ok = False
                    while not ok:
                        userInput = raw_input("Is this ok? (Y/N) ")
                        if (userInput == "Y" or userInput == "y"):
                            ok=True
                            b.insertWord(word, loc, orientation, debug = options.boss)
                            print "move successful"
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
                                    tiles.append(b.bag.getLetter())
                                
                            scoreOpp += score
                            print b
                            valid = True
                            turn = not turn
                        elif (userInput == "N" or userInput == "n"):
                            print "Try Again"
                            break
                        else: 
                            print "Invalid Input"
                else:
                    print "Invalid word!"
            
        print "AI: %s, You: %s"% (scoreMe, scoreOpp)

main()
