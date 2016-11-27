import board
import agent
import copy

def main():
    b = board.Board()
    AI = agent.Agent(b)
    scoreYou = 0
    scoreMe = 0
    letterMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14}
    print b
    for i in xrange(0, 1):
        you = open("/home/cjoseph/Documents/quackle/test/quackgame-%i.gcg"%i,'r')
        me = open("/home/cjoseph/Documents/quackle/test/cs221game-%i"%i,'w+')
        turn = False
        yourMove = ""
        myMove = ""
        while True:
            y = you.readline().strip()
            #m = me.readline().strip()
            if y != yourMove and y != "":
                yourMove = y.split()
                player = yourMove[0]
                if player == "quackle":
                    orientation= yourMove[1] #TODO: make sure this works
                    word = yourMove[3].upper()
                    loc = (int(yourMove[2][0:-1])-1, letterMap[yourMove[2][-1]])
                    print "word, loc, score:",word,loc,orientation,scoreYou
                    scoreYou += b.insertWord(word, loc, orientation, debug = False)
                    
                elif player == "cs221":
                    rack = yourMove[-1]
                    (word, loc, orientation, usedTiles, score) = AI.quackleMove([t for t in rack])
                    scoreMe += score
                    #write move to file
                    # TODO: fix format of word and loc to match quackle's
                    me.write("%s %s %s\n"%(word, loc, orientation))
                    me.flush()
                print b
                print "CS221: %s, Quackle: %s"% (scoreMe, scoreYou)
            #if m != myMove and m != "":
                #myMove = m.split()
                #print "myMove",myMove
            
            #print m

        # else: #other goes
        #     valid = False
        #     while not valid:
        #         if options.human: print "Tiles:",tiles
        #         userInput = raw_input("Enter a word, (row,col) and orientation 'h' or 'v': ")
        #         inputList = userInput.split()
        #         if len(inputList) != 3:
        #             print "Invalid input format, try again!"
        #             continue
        #         #parse stuff
        #         word = inputList[0].upper()
        #         try:
        #             #very dangerous, LOL!
        #             loc = eval(inputList[1])
        #         except:
        #             print "could not parse location to tuple format!"
        #             continue
                
        #         if len(loc) != 2:
        #             print "invalid (row,col):",loc
        #             continue
                
        #         orientation = inputList[2].lower()
        #         if orientation != 'v' and orientation != 'h':
        #             print "invalid orientation:",orientation
        #             continue
        #         #b.score
        #         #if not sure, break out of if
        #         score = b.score(word, loc, orientation)
        #         print score
        #         if options.boss or score > -1:
        #             #make a copy of board and insert to preview move
        #             b2 = copy.deepcopy(b)
        #             b2.insertWord(word, loc, orientation, debug = options.boss)
        #             print b2
        #             print "Move Score= ", score
        #             ok = False
        #             while not ok:
        #                 userInput = raw_input("Is this ok? (Y/N) ")
        #                 if (userInput == "Y" or userInput == "y"):
        #                     ok=True
        #                     b.insertWord(word, loc, orientation, debug = options.boss)
        #                     print "move successful"
        #                     #does not account for the case where a letter on
        #                     #the board also appears in the tile
        #                     #set... eit. We'll mostly be doing AI vs AI anyway
        #                     if options.human:
        #                         r = 0
        #                         for l in word:
        #                             if l in tiles:
        #                                 tiles.remove(l)
        #                                 r += 1
        #                         for i in xrange(r):
        #                             tiles.append(b.bag.getLetter())
                                
        #                     scoreOpp += score
        #                     print b
        #                     valid = True
        #                     turn = not turn
        #                 elif (userInput == "N" or userInput == "n"):
        #                     print "Try Again"
        #                     break
        #                 else: 
        #                     print "Invalid Input"
        #         else:
        #             print "Invalid word!"
            


main()
