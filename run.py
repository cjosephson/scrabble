import board
import baseline
import humanfriendly

def main():
    b = board.Board()
    AI = baseline.Baseline(b)
    scoreOpp = 0
    scoreMe = 0
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

                score = b.insertWord(word, loc, orientation)
                if score > -1:
                    scoreOpp += score
                    print b
                    valid = True
                else:
                    print "Invalid word!"
            turn = not turn
        print "AI: %s, Opponent: %s"% (scoreMe, scoreOpp)

main()
