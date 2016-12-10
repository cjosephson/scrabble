#import numpy as np
import copy
import letterbag
from util import *

class Board:
    NORMAL = 'normal'
    DOUBLEWORD = 'doubleword'
    TRIPLEWORD = 'tripleword'
    DOUBLELETTER = 'doubleletter'
    TRIPLELETTER = 'tripleletter'
    
    def __init__(self):
        self.board=[]
        self.bag = letterbag.LetterBag()
        for i in xrange(15):
            self.board.append([(' ', Board.NORMAL) for i in xrange(15)])
        self.dictionary = {}
        #load in dictionary
        f = file('scrabblewords.txt','r')
        for w in f:
            self.dictionary[str.strip(w)] = True

        #------------BONUS SQUARES------------------		
	triplewords = [(0,0), (7,0), (14,0), (0,7), (14,7), (0,14), (7,14), (14,14)]	
	for (x, y) in triplewords:
	    self.board[x][y] = (' ', Board.TRIPLEWORD)
	    
	doublewords = [(1,1), (2,2), (3,3), (4,4), (1,13), (2,12), (3,11), (4,10),
		       (13,1), (12,2), (11,3), (10,4), (13,13), (12,12), (11,11), (10,10),
					   (7,7)]
	for (x, y) in doublewords:
	    self.board[x][y] = (' ', Board.DOUBLEWORD)
			
	tripleletters = [(5,1), (9,1), (1,5), (1,9), (5,13), (9,13), (13,5), (13,9),
			 (5,5), (9,9), (5,9), (9,5)]
	for (x, y) in tripleletters:
	    self.board[x][y] = (' ', Board.TRIPLELETTER)
		
	doubleletters = [(3,0), (0,3), (11,0), (0,11), (3,14), (11,14), (14,3), (14,11),
			 (2,6), (3,7), (2,8), (6,2), (7,3), (8,2), (6,12), (7,11), (8,12),
			 (12,6), (11,7), (12,8), (6,6), (8,8), (6,8), (8,6)]
	for (x, y) in doubleletters:
	    self.board[x][y] = (' ', Board.DOUBLELETTER)
	# #-----------------------------------------
	

    def __str__(self):
        mults = {Board.NORMAL: ' ', Board.DOUBLELETTER:' ', Board.DOUBLEWORD:' ',
                 Board.TRIPLELETTER:' ', Board.TRIPLEWORD:' '}
        #mults = {Board.NORMAL: ' ', Board.DOUBLELETTER:'2', Board.DOUBLEWORD:'*',
        #         Board.TRIPLELETTER:'3', Board.TRIPLEWORD:'&'}
        s = ''
        for i in xrange(len(self.board)):
            s += ("%02d"%(i))+": "+str([mults[b[1]] if b[0] == ' ' else  b[0]
                                        for b in self.board[i]])+'\n'
        s+="     "
        for i in xrange(15):
            s+=("|%02d| "%(i))
        #s+="\nLegend: 2=double letter, *=double word, 3=triple letter, &=triple word"
        return s

    '''Given a word, a start point, and an orientation, return a score for
    filling in that word. If the word is invalid (e.g. too long, or
    causes invalid words in the orthogonal dimension), it returns -1.
    '''
    def score(self, word, startPoint, orientation):
        #return self.oldScore(word, startPoint, orientation)
        #print 'score start'
        #if not self.valid(word, startPoint, orientation):
        #    return -1
        # print 'score start'
        y,x = startPoint
        #print word, len(word), x, y, orientation
        #print y,x, len(word), (len(word) + x)
        if (orientation == "h") and (len(word)+x-1 > 15):
            print "exceeded horizontal len check"
            return -1 
        # print "pt A"
        if (orientation == "v") and (len(word)+y-1 > 15):
            print "exceeded vert len check"
            return -1
        # print "pt b"
        wordsFormed = []
        wordsFormed.append((word, startPoint, orientation)) 
        s = 0
        wordMult = 1
        y,x = startPoint
        originalLen = 0
        if orientation == "h":
            #print 'pos:', y,x
            for i in xrange(len(word)):
                if i+x < 15:
                    c = self.getCol(i+x)
                    #print i+x
                    if c[y][0] != " ": originalLen +=1
                    partialWord = word[i]
                    cont = True
                    pos1 = 1;
                    if y > 0:
                        l = c[y-1][0] 
                        if l == " ": cont = False
                        while(cont):
                          #  print pos
                            partialWord = l + partialWord
                            pos1 +=1
                        
                            if y - pos1 > -1: l = c[y-pos1][0] 
                            if l == " ": cont = False
                            if y - pos1 == -1: cont = False
                    pos = 1;
                    if y < 14:
                        l = c[y+1][0] 
                        cont = True
                        if l == " ": cont = False
                        while(cont):
                       #     print pos
                            partialWord = partialWord + l
                            pos +=1
                            if y+pos < 15: l = c[y+pos][0] 
                            if l == " ": cont = False
                            if y+pos == 15: cont = False
                    #print partialWord, self.board[y][i+x][0]
                    if len(partialWord) > 1 and self.board[y][i+x][0] == " ": 
                     #   print i+x, y, c[y][0]
                        wordsFormed.append((partialWord, (y-pos1, i+x), 'v'))
        elif orientation == "v":
            for i in xrange(len(word)):
                if i+y < 15:
                    c = self.getRow(i+y)
                    if c[x][0] != " ": originalLen +=1
                    partialWord = word[i]
                    cont = True
                    pos1 = 1;
                    if x > 0:
                        l = c[x-1][0] 
                        if l == " ": cont = False
                        while(cont):
                            partialWord = l + partialWord
                            pos1 +=1
                            if x-pos1 > -1: l = c[x-pos1][0] 
                            if l == " ": cont = False
                            if x-pos1 == -1: cont = False
                    pos = 1;
                    if x < 14:
                        l = c[x+1][0] 
                        cont = True
                        if l == " ": cont = False
                        while(cont):
                            partialWord = partialWord + l
                            pos +=1
                            if x+pos < 15: l = c[x+pos][0] 
                            if l == " ": cont = False
                            if x+pos == 15: cont = False
                    if len(partialWord) > 1 and self.board[i+y][x][0] == " ":
                        wordsFormed.append((partialWord,(i+y, x-pos1),'h'))
        sum = 0
        if len(word) - originalLen == 7: sum += 50
        for w in wordsFormed:
            (crossword, sp, or2) = w
            val = self.rawScore(crossword, sp, or2)
            if val == -1: return -1
            sum += val
        return sum

    def rawScore(self, word, startPoint, orientation):
        #if not self.valid(word, startPoint, orientation):
        #    return -1
        if (word not in self.dictionary.keys()) and (len(word) > 1):
            return -1
        
        mults = {Board.NORMAL:1, Board.DOUBLELETTER:2, Board.DOUBLEWORD:3,
                 Board.TRIPLELETTER:3, Board.TRIPLEWORD:3}
        
        s = 0
        wordMult = 1
        col,row = startPoint
        for c in word:
            if row > 14 or col > 14:
                print "lol1",word
                return -1
            
            tile = self.board[row][col]
            if tile[0] == ' ':
                if tile[1] in [Board.TRIPLEWORD, Board.DOUBLEWORD]:
                    wordMult = mults[tile[1]]
                    s+=letterToPoints[c]
                else: #it's just a letter multiplier
                    s+=letterToPoints[c]*mults[tile[1]]
            else:
                    s+=letterToPoints[c]
            if orientation == 'h':
                row += 1
            else:
                col += 1
        return s*wordMult   
    
    def humanValid(self, word, startPoint, orientation, tiles):
        #tile check
        tile = True
        pos = startPoint
        for c in word:
            if c not in tiles:
                if c != self.getChar(pos):
                    tile = False
                    #print "failed tile check!"
                    break
            if orientation == 'h':
                pos = (pos[0], pos[1] + 1)
            else:
                pos = (pos[0] +1, pos[1])
        #crosscheck
        cross = self.valid(word, startPoint, orientation)
        return tile and cross

    def valid(self, word, startPoint, orientation):
        (ri, ci) = startPoint
        if orientation == 'h':
            #check bounds
            #print "ci, ci+len = %s, %s"%(ci, ci+len(word))
            if ci + len(word) > 15:
                #print "fails fit check horizontally"
                return False
            
            #check that the word satisfies column constraints
            row = [i for i in self.board[ri]]
            wi = 0
            l = len(word)
            #print "range",range(ri, ri+len(word))
            for i in xrange(ci, ci+len(word)):
                #print "r[%i], word[%i] = %s, %s"%(i, wi, row[i], word[wi])
                if row[i][0] == word[wi]:
                    l -= 1
                elif row[i][0] != ' ' and row[i][0] != word[wi]:
                    #print "row constraints not satisfied"
                    return False
                row[i] = (word[wi], row[i][1])
                wi += 1
            #print "l",l 
            #if l > 7:
            #    return False
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
                col =  self.getCol(i)
                letters = [t[0] for t in col]
                if not self.validWords(letters):
                    #print "cross check fails col %i: %s"%(i,letters) 
                    self.board[ri] = oldrow
                    return False
            #add row back because we're just doing a validity check
            self.board[ri] = oldrow
                
        elif orientation == 'v':
            #check bounds
            #print "ri, ri+len = %s, %s"%(ri, ri+len(word))
            if ri + len(word) > 15:
                #print "fails fit check vertically"
                return False
            #check that the word satisfies column constraints
            #print "ci: %s, col: %s"%(ci, self.getCol(ci))
            col = [i for i in self.getCol(ci)]
            wi = 0
            l = len(word)
            #print "word",word
            #print "range",range(ri, ri+len(word))
            #print "col_%i %s"%(ci, [c[0] for c in col])
            for i in xrange(ri, ri+len(word)):
                #print "col[%s], word[%s] = %s,%s"%(i, wi, col[i][0], word[wi])
                if col[i][0] == word[wi]:
                    l -= 1
                elif col[i][0] != ' ' and col[i][0] != word[wi]:
                    #print "col constraints false"
                    return False
                col[i] = (word[wi], col[i][1])
                wi += 1
            #print "l",l
            #if l > 7:
            #   return False

            #a word not in the dictionary
            if not self.validWords(col):
                #print "not in dict",col
                return False

            #check that we didn't make non-words in the other
            #dimension
            oldBoard = copy.deepcopy((self.board)) #copy/deep copy might be needed?
            #print "range",range(ri, ri+len(word))
            for i in xrange(ri, ri+len(word)):
                row =  self.board[i]
                row[ci] = col[i] #add our new char
                letters = [t[0] for t in row]
                if not self.validWords(letters):
                    #print "cross check fails row %i: %s"%(i,letters)
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
        for w in ''.join([s[0] for s in l]).split():
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

    def getChar(self, pos):
        x,y = pos
        if x > 14 or y > 14:
            return ''
        return self.board[x][y][0]

    def insertChar(self, c, pos):
        x,y = pos
        if x > 14 or y > 14:
            return
        self.board[x][y] = (c, self.board[x][y][1])

    def insertWord(self, word, startPoint, orientation, debug = False):
        (ri, ci) = startPoint
        score =  self.score(word, startPoint, orientation)
        #print "insertWord",word, score, score > 0
        wi = 0
        if not debug and score < 0:
            return score
        
        if orientation == 'h':
             #print "range",range(ri, ri+len(word))
            for i in xrange(ci, ci+len(word)):
                #print "inserting %s at (%s,%s)"%(word[wi], ri, i)
                self.insertChar(word[wi], (ri, i))
                wi += 1
        elif orientation == 'v':
            for i in xrange(ri, ri+len(word)):
                #print "inserting %s at (%s,%s)"%(word[wi], ri, i)
                self.insertChar(word[wi], (i, ci))
                wi += 1
        else:
            raise Exception("Invalid orientation:",orientation)
        #print "Inserted %s at %s %s-ly"%(word, startPoint, orientation) 
        return score

    # def oldScore(self, word, startPoint, orientation):
    #     if not self.valid(word, startPoint, orientation):
    #         return -1
    #     if (word not in self.dictionary.keys()) and (len(word) > 1):
    #         return -1
        
    #     mults = {Board.NORMAL:1, Board.DOUBLELETTER:2, Board.DOUBLEWORD:3,
    #              Board.TRIPLELETTER:3, Board.TRIPLEWORD:3}
        
    #     s = 0
    #     wordMult = 1
    #     y,x = startPoint
    #     for c in word:
    #         if x > 14 or y > 14: return -1
         
    #         tile = self.board[y][x]
         
    #         if tile[0] == ' ':
    #             if tile[1] in [Board.TRIPLEWORD, Board.DOUBLEWORD]:
    #                 wordMult = mults[tile[1]]
    #                 s+=letterToPoints[c]
    #             else: #it's just a letter multiplier
    #                 s+=letterToPoints[c]*mults[tile[1]]
    #         else:
    #                 s+=letterToPoints[c]
    #         if orientation == 'h':
    #             x += 1
    #         else:
    #             y += 1
        
    #     return s*wordMult
