#import numpy as np
import copy
import oracle
import baseline

class Board:
    def __init__(self):
        self.board=[]
        for i in xrange(15):
            self.board.append([(' ') for i in xrange(15)])
        self.dictionary = {}
        #load in dictionary
        f = file('scrabblewords.txt','r')
        for w in f:
            self.dictionary[str.strip(w)] = True

    def __str__(self):
        s = ''
        for i in xrange(len(self.board)):
            s += ("%02d"%(i))+": "+str(self.board[i])+'\n'
        s+="     "
        for i in xrange(15):
            s+=("|%02d| "%(i))
        return s

    '''Given a word, a start point, and an orientation, return a score for
    filling in that word. If the word is invalid (e.g. too long, or
    causes invalid words in the orthogonal dimension), it returns -1.
    '''
    def score(self, word, startPoint, orientation):
        if not self.valid(word, startPoint, orientation):
            return -1
        letterToPoints = {'W':2, 'D':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'Y':4,
			  'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10,'A':1, 'E':1, 'I':1, 'O':1, 'N':1, 
			  'R':1, 'T':1, 'L':1, 'S':1, 'U':1, 'G':3}
	s = 0
	for c in word: s+=letterToPoints[c]
	return s	

    def valid(self, word, startPoint, orientation):
        (ci, ri) = startPoint
        if orientation == 'h':
            #check bounds
            if ci + len(word) >= 15:
                #print "fails fit check horizontally"
                return False
            
            #check that the word satisfies column constraints
            row = [i for i in self.board[ri]]
            wi = 0
            l = len(word)
            #print "range",range(ri, ri+len(word))
            for i in xrange(ci, ci+len(word)):
                #print "r[%i], word[%i] = %s, %s"%(i, wi, row[i], word[wi])
                if row[i] == word[wi]:
                    l -= 1
                elif row[i] != ' ' and row[i] != word[wi]:
                    #print "row constraints not satisfied"
                    return False
                row[i] = word[wi]
                wi += 1
            #print "l",l 
            if l > 7:
                return False
            #make sure we don't have any adjacent letters that create
            #a word not in the dictionary
            if not self.validWords(row):
                #print "row validity failed!",row
                return False
            
            #check that we didn't make non-words in the other
            #dimension
            oldrow = self.board[ri]
            self.board[ri] = row
            for i in xrange(15):
                col = self.getCol(i)
                if not self.validWords(col):
                    #print "cross check fails col %i: %s"%(i,col) 
                    self.board[ri] = oldrow
                    return False
            #add row back because we're just doing a validity check
            self.board[ri] = oldrow

                
        elif orientation == 'v':
            #check bounds
            #print "ri, ri+len = %s, %s"%(ri, ri+len(word))
            if ri + len(word) >= 15:
                #print "fails fit check vertically"
                return False
            #check that the word satisfies column constraints
            col = [i for i in self.getCol(ci)]
            wi = 0
            l = len(word)
            #print "range",range(ri, ri+len(word))
            for i in xrange(ri, ri+len(word)):
                if col[i] == word[wi]:
                    l -= 1 
                elif col[i] != ' ' and col[i] != word[wi]:
                    #print "col constraints false"
                    return False
                #print "i, wi = %s,%s"%(i, wi)
                col[i] = word[wi]
                wi += 1
            #print "l",l
            if l > 7:
                return False

            #a word not in the dictionary
            if not self.validWords(col):
                #print "not in dict",col
                return False

            #check that we didn't make non-words in the other
            #dimension
            oldBoard = copy.deepcopy((self.board)) #copy/deep copy might be needed?
            #print "range",range(ri, ri+len(word))
            for i in xrange(ri, ri+len(word)):
                row = self.board[i]
                row[ci] = col[i] #add our new char
                if not self.validWords(row):
                    #print "cross check fails row %i: %s"%(i,row)
                    self.board = oldBoard
                    #print self.__str__()
                    return False
                else:
                    self.board[i] = row
            # return board to original state because we're just doing
            # a validity check
            self.board = oldBoard
        return True
    
    def validWords(self, l):
        for w in ''.join(l).split():
            if w not in self.dictionary and len(w)>1:
                return False
        return True
        
    def getRow(self, ri):
        if ri <15:
            return self.board[ri]
        else: return None

    def getCol(self, ci):
        col = None
        if ci < 15:
            col = [self.board[i][ci] for i in xrange(15)]
        return col
    
