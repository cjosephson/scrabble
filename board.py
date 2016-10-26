#import numpy as np

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
        for r in self.board:
            s += str(r)+'\n'
        return s

    '''Given a word, a start point, and an orientation, return a score for
    filling in that word. If the word is invalid (e.g. too long, or
    causes invalid words in the orthogonal dimension), it returns -1.
    '''
    def score(self, word, startPoint, orientation):
        if not self.valid(word, startPoint, orientation):
            return -1
        s = 22
        return s

    def valid(self, word, startPoint, orientation):
        (ci, ri) = startPoint
        if orientation == 'h':
            #check bounds
            if ci + len(w) >= 15:
                return -1
            
            #check that the word satisfies column constraints
            row = [i for i in self.board[ri]]
            wi = 0
            for i in xrange(ci, ci+len(word)):
                if row[i] != ' ' and row[i] != word[wi]:
                    return -1
                else:
                    row[i] = word[wi]
                    wi += 1
            #make sure we don't have any adjacent letters that create
            #a word not in the dictionary
            if not self.validWords(row):
                return -1
            
            #check that we didn't make non-words in the other
            #dimension
            oldrow = self.board[ri]
            self.board[ri] = row
            for i in xrange(15):
                col = getCol(i)
                if not self.validWords(col):
                    self.board[ri] = oldrow
                    return -1
            #add row back because we're just doing a validity check
            self.board[ri] = oldrow
                
        elif orientation == 'v':
            #check bounds
            if ri + len(w) >= 15:
                return -1

            #check that the word satisfies column constraints
            col = [i for i in getCol(ci)]
            wi = 0
            for i in xrange(ri, ri+len(word)):
                if col[i] != ' ' and col[i] != word[wi]:
                    return -1
                else:
                    col[i] = word[wi]
                    wi += 1

            #a word not in the dictionary
            if not self.validWords(col):
                return -1

            #check that we didn't make non-words in the other
            #dimension
            oldBoard = self.board #copy/deep copy might be needed?
            for i in xrange(ri, ri+len(word)):
                row = self.board[i]
                row[ci] = col[i] #add our new char
                if not self.validWords(row):
                    self.board = oldBoard
                    return -1
                else:
                    self.board[i] = row
            # return board to original state because we're just doing
            # a validity check
            self.board = oldBoard
    def validWords(self, l):
        for w in ''.join(l).split():
            if w not in self.dictionary:
                return False
        return True
        
    def getRow(self, ri):
        if ri <15:
            return self.Board[ri]
        else: return None

    def getCol(self, ci):
        col = None
        if ci < 15:
            col = [self.board[i][ci] for i in xrange(15)]
        return col
    
b = Board()

b.board[4][4] = ('S')
b.board[5][4] = ('T')
b.board[6][4] = ('A')
b.board[7] = [(' '),(' '),(' '),('U'),('N'),('I'),('V'),('E'),('R'),('S'),('I'),('T'),('Y'),(' '),(' ')]
b.board[8][4] = ('F')
b.board[9][4] = ('O')
b.board[10][4] = ('R')
b.board[11][4] = ('D')
print b
