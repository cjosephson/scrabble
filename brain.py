import treeBuilder
import board
import pygtrie


##################################
# Appel Jaconson Algorithm Bits
################################

#########################################################
# generate moves -> 
# generateMoves(self, rack) where rack is list of tiles = characters
# return (string, v/h, starting[row][col],
# what characters were used from the rack)
##########################################################


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',\
			'H', 'I', 'J', 'K', 'L', 'M', 'N',\
			'O', 'P', 'Q', 'R', 'S', 'T', 'U',\
			'V', 'W', 'X', 'Y', 'Z']


class AJalgorithm:
	def __init__(self, board):
		self.board = board
		self.trie = treeBuilder.lexTree

	# Returns true if all words in string are words
	def isValidWordString(self, string):
		valid = True
		strList = string.split()
		for s in strList:
			if len(s) > 1: 
				value = self.trie.get(s)
				if value is None:
					valid = False
		return valid
##############################################
# Crosschecks
# 
# Performs crosschecks on a given row/column
# input:: row/col # 
# returns dict of possible letters for each 
#   square in row/col
#
# TO DO: fix this so that it only updates 
# relevant bits after each turn 
################################################
	
	def crosschecks(self, row, orientation): 
		validLetters = {}
		if orientation == "h":
			for i in range(15):
				colString = []
				letterList = []
				for square in self.board.getCol(i):
					colString.append(square[0])
				print i, colString
				if colString[row] == " ":
					for c in range(26):
						colString[row] = alphabet[c]
						if self.isValidWordString("".join(colString)):
							print "".join(colString)
							letterList.append(alphabet[c])
						colString[row] = " "
				validLetters[i] = list(letterList)
		else:
			for i in range(15):
				rowString = []
				letterList = []
				for square in self.board.getRow(i):
					rowString.append(square[0])
				if rowString[row] == " ":
					for c in range(26):
						rowString[row] = alphabet[c]
						if self.isValidWordString("".join(rowString)):
							letterList.append(alphabet[c])
						rowString[row] = " "
				validLetters[i] = list(letterList)
		return validLetters 

	###################################
	# findAnchors
	#
	# returns list of anchors the board
	###################################	
	def findAnchors(self):
		anchorList = []; 
		for i in range(15):
			rowString = []
			colString = []
			#check through rows
			for square in self.board.getRow(i):
				rowString.append(square[0])
			#print rowString
			for square in self.board.getCol(i):
					colString.append(square[0])
			for j in range(14):
				if (rowString[j] == " " and rowString[j+1] != " "):
					print i,j
					if (i,j) not in anchorList:
			#			print 'huh', (i,j)
						anchorList.append((i,j))
				if (colString[j] == " " and colString[j+1] != " "):
					if (j,i) not in anchorList:
						anchorList.append((j,i))
			#	print anchorList
		return anchorList
			#check through cols

#############################
b =board.Board()
alg = AJalgorithm(b)

b.insertWord("AT", (0,11), "v")
b.insertWord("HELLO", (7,7), "h")
print b
print alg.findAnchors()

