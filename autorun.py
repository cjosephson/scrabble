import board
import agent
import copy

def main():
    b = board.Board()
    AI = agent.Agent(b)
    scoreYou = 0
    scoreMe = 0
    letterMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
                 0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O'}
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
                    print "quackle move",yourMove
                    orientation= yourMove[1]
                    loc = (int(yourMove[2]), int(yourMove[3]))
                    word = yourMove[4].upper()
                    print "word, loc, score:",word,loc,orientation,scoreYou
                    scoreYou += b.insertWord(word, loc, orientation, debug = False)
                    
                elif player == "cs221":
                    rack = yourMove[-1]
                    (word, (row,col) , orientation, usedTiles, score) = AI.quackleMove([t for t in rack])
                    scoreMe += score
                    #write move to file
                    # TODO: fix format of word to match quackle's; wildcard fills are lowercase
                    me.write("%s %s %s %s\n"%(word, row, col, orientation))
                    me.flush()
                print b
                print "CS221: %s, Quackle: %s"% (scoreMe, scoreYou)

main()
