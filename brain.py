import treeBuilder
import board
import pygtrie


##################################
# Appel Jaconson Algorithm Bits
################################


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',\
			'h', 'i', 'j', 'k', 'l', 'm', 'n',\
			'o', 'p', 'q', 'r', 's', 't', 'u',\
			'v', 'w', 'x', 'y', 'z']


class AJalgorithm:
	def __init__(self, board):
		self.board = board
		self.trie = treeBuilder.lexTree
##############################################
# Crosschecks
# 
# Performs crosschecks on a given row/column
# input:: row/col # 
# returns dict of possible letters for each 
#   square in row/col
################################################
	
	# Returns true if all words in string are words
	def isValidWordString(self, string):
		valid = True
		strList = string.split()
		for s in strList: 
			value = self.trie.get(s)
			if value is None:
				valid = False
		return valid

	def crosschecks(self, row, orientation): 
		validLetters = {}
		if orientation == "h":
			for i in range(15):
				if self.board[row][i] == " ":
					letterList = []
					for c in range(26):
						self.board[row][i] = alphabet[c]
						#convert col to string
						colString = ""
						for square in self.board.getCol(i):
							colString = colString + square[0]
						if isValidWordString(colString):
							letterList.append(alphabet[c])
					validLetters[i] = list(letterList)

				else:
					#if you use this, something's gone wrong
					validLetters[i] == None 
		return validLetters 




############
#tests
###########

b = board.Board()
#print b.getCol(1)
alg = AJalgorithm(b)

print alg.crosschecks(1,"h")