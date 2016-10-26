
##CS221 final project oracle



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
	def OracleMove(self, board):
		
		#find possible moves to get the highest score
		maxScore = 0
		possibleMoves = [] 
		for word in dictionary.keys():
			if score(word) > maxScore:
					possibleMoves = []
					for vector in self.board.getColumns():
						tempResults = convolve(word, vector)
						for r in tempResults: possibleMoves.append(r)
					for vector in self.board.getRows():
						tempResults = convolve(word, vector)
						for r in tempResults: possibleMoves.append(r)
		
		#find result with highest score
		(word, startIndex, vecetorID) = possibleMoves[0]

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
# list of (word, startIndex, vectorID, orientation)
#####################################################
def convolve(word, vector, vecetorID): 
	#vector should be string length 15
	
	results = []

	#turns vector into a string
	vectorString = ""
	for c in vector:
		vectorString += c

	print "|"+vectorString+"|"
	
	#if column blank, can't build on anything
	if (vectorString == "               "):
			return False	

	l = len(word)
	for i in range(len(vectorString)-len(word)):
		print word, vectorString[i:i+l]
		if isSubstring(word, vectorString[i:i+l]):
			print "TRUE"
			results.append((word, i, vecetorID))
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
	print convolve("but", [" ", " "," ", " ", " ", " ", " ", " ", " ", "b", " ", "t", " ", " ", " "])