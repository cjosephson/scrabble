##CS221 final project oracle
from operator import itemgetter



#####################################################
# Oracle: 
# Upper bound metric on best possible move. 
# Very upper. Slow AF
#####################################################
class Oracle:
	def __init__(self, board):
		self.board = board
	#####################################################
	# Score: 
	# Returns the base score of a word (no multipliers)
	# currently assumes no multiplier tiles for discarding
	# keys
	#####################################################		
	def move(self):
		board=self.board
		#find possible moves to get the highest score
		possibleMoves = [] 
		for word in board.dictionary.keys():
			for i in xrange(15):
                                col = [c[0] for c in self.board.getCol(i)]
				#print "col",col
                                #(word, startIndex, vectorID)
                                results = convolve(word, col)
                                if results != None:
				        for r in results:
                                                (word, startIndex) = r
                                                score = self.board.score(word, (i, startIndex), 'v')
                                                if score  > -1:
                                                        possibleMoves.append((word, score, (i, startIndex), 'v'))
			for i in xrange(15):
                                row = [r[0] for r in self.board.getRow(i)]
                                results = convolve(word, row)
                                if results != None:
				        for r in results:
                                                (word, startIndex) = r
                                                score = self.board.score(word, (startIndex, i ), 'h')
                                                if score > -1:
                                                        possibleMoves.append((word, score, (startIndex, i ), 'h'))

                #print possibleMoves
		#find result with highest score
		(word, score, startPoint, orientation) = max(possibleMoves, key=itemgetter(1))
                
                print "ORACLE: max word is %s with score %i at %s,%s"%(word, score,startPoint,orientation) 
		#add it to the board

		return None
#####################################################
# Score: 
# Returns the base score of a word (no multipliers)
#####################################################
def score(word):
	letterToPoints = {'W':2, 'D':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'Y':4,
					  'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10,'A':1, 'E':1, 'I':1, 'O':1, 'N':1, 
					  'R':1, 'T':1, 'L':1, 'S':1, 'U':1, 'G':3}
	sum = 0
	for c in word: sum +=letterToPoints[c]
	return sum	

#####################################################
# Convolves: 
# returns options for fitting a word into a 
# row/column vector
# list of (word, startIndex)
#####################################################
def convolve(word, vector): 
	#vector should be string length 15
	
	results = []

	#turns vector into a string
	vectorString = ""
	for c in vector:
		vectorString += c

	#print "|"+vectorString+"|"
	
	#if column blank, can't build on anything
	if (vectorString == "               "):
			return None

	l = len(word)
	for i in range(len(vectorString)-len(word)):
		#print word, vectorString[i:i+l]
		if isSubstring(word, vectorString[i:i+l]):
			#print "TRUE"
			results.append((word, i))
	return results



def isSubstring(word, sub):
	if len(sub) != len(word): return False
	result = True
	allBlank = True
	for i in range(len(word)):
		if (sub[i] != " "):
				allBlank = False
				if (sub[i] != word[i]):
					result = False
					break;  
	return (result and not allBlank)


if __name__ == '__main__':
        pass
	#print convolve("but", [" ", " "," ", " ", " ", " ", " ", " ", " ", "b", " ", "t", " ", " ", " "])
        
