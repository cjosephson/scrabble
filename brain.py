import treeBuilder
import board
import pygtrie
import pdb

##################################
# Appel Jaconson Algorithm Bits
################################

#########################################################
# generate moves -> 
# generateMoves(self, rack) where rack is list of tiles = characters
# return (string, v/h, starting[row][col],
# what characters were used from the rack)
##########################################################

_SENTINEL =  object()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',\
			'H', 'I', 'J', 'K', 'L', 'M', 'N',\
			'O', 'P', 'Q', 'R', 'S', 'T', 'U',\
			'V', 'W', 'X', 'Y', 'Z']


class AJalgorithm:
	def __init__(self, board):
		self.board = board
		self.trie = treeBuilder.lexTree
		self.LegalMoves = set() #list of legal moves. gets changed every time getMove is called
		self.rack = []
		self.crosscheckList = {} #dictionary of crosschec,s for every square

		for row in range(15):
			self.crosscheckList[row] = {}
			for col in range(15):
				self.crosscheckList[row][col] = []

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
				if colString[row] == " ":
					for c in range(26):
						colString[row] = alphabet[c]
						if self.isValidWordString("".join(colString)):
							letterList.append(alphabet[c])
						colString[row] = " "
				validLetters[i] = list(letterList)
			self.crosscheckList[row] = validLetters
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
				self.crosscheckList[i][row] = list(letterList)
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
			for square in self.board.getRow(i):
				rowString.append(square[0])
			for square in self.board.getCol(i):
				colString.append(square[0])
			for j in range(14):
				if (rowString[j] == " " and rowString[j+1] != " "):
					if (i,j) not in anchorList:
						anchorList.append((i,j))
				if (colString[j] == " " and colString[j+1] != " "):
					if (j,i) not in anchorList:
						anchorList.append((j,i))
		return anchorList
			#check through cols
	######################################
	# ExtendRight
	#
	# recursive call that does stuff
	#  
	######################################		
	def ExtendRight(self, PartialWord, node, square, startSquare, orientation):
		edges = node.children.keys()
		(row, col) = square
		squareVal = b.board[row][col][0]
		#print PartialWord
		#print "edges", edges
		#print square

		if orientation == "h": nextSquare = (row, col+1)
		if orientation == "v": nextSquare = (row+1, col)
		#print nextSquare
		if squareVal == " ":
			if type(node.value) is not type(_SENTINEL):
				self.LegalMoves.add((PartialWord, startSquare, orientation))
			for l in edges:
				if l in self.rack:
					if l in self.crosscheckList[row][col]:
						self.rack.remove(l)
						newNode = node.children[l]
						self.ExtendRight(PartialWord+l, newNode, nextSquare, startSquare, orientation)
						self.rack.append(l)

		else:
			#print "here"
			l = squareVal
			#print "X"+l+"X"
			if l in edges: 
				newNode = node.children[l]
				self.ExtendRight(PartialWord+l, newNode, nextSquare, startSquare, orientation)

        ######################################
	# ExtendLeft
	#
	# recursive call that does left stuff
	#  
	######################################		
	def ExtendLeft(self, PartialWord, node, limit,
                       anchorSquare,startSquare, orientation):
                #call crosscheck before calling extendLeft or
                #extendRight
                row, col = startSquare
                self.crosschecks(row, orientation)
                self.ExtendRight(PartialWord, node, anchorSquare,
                                 startSquare, orientation)
                if limit > 0:
                        nextSquare = ((row, col-1) if orientation == "h"
                                     else (row-1, col))
                
                        edges = node.children.keys()
                        for l in edges:
                                if l in self.rack:
					self.rack.remove(l)
					newNode = node.children[l]
					self.ExtendLeft(PartialWord+l,
                                                        newNode, limit-1,
                                                        anchorSquare,
                                                        nextSquare,
                                                        orientation)
					self.rack.append(l)

                                

#############################
#tests
b =board.Board()
alg = AJalgorithm(b)

b.insertWord("HELLO", (7,7), "h")
b.insertWord("WORLD", (6,11), "v")
b.insertWord("STANFORD", (1,1), "h")
print b
anchors = alg.findAnchors()
assert anchors == [(1, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (6, 10), (0, 7), (7, 6), (6, 7), (0, 8), (6, 8), (8, 10), (6, 9), (9, 10), (10, 10), (5, 11)]

h = {}
v = {}
for (r,c) in anchors:
        if r not in h:
                h[r] = True
        if c not in v:
                v[c] = True

for r in h.iterkeys():
        alg.crosschecks(r,'h')
for c in v.iterkeys():
        alg.crosschecks(c, 'v')
print "-------------------------"
print "crosschecks 6,h"
assert alg.crosschecks(6, "h") == {0: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 1: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 2: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 3: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 4: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 5: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 6: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 7: ['A', 'E', 'O', 'S', 'U'], 8: ['A', 'B', 'D', 'F', 'H', 'M', 'N', 'O', 'P', 'R', 'W', 'Y'], 9: ['A', 'E'], 10: ['A', 'E'], 11: [], 12: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 13: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 14: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']}

print "crosschecks 11,v"
assert alg.crosschecks(11, "v") == {0: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 1: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 2: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 3: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 4: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 5: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 6: [], 7: [], 8: [], 9: [], 10: [], 11: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 12: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 13: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 14: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']}

print "crosschecks 10,h"
assert alg.crosschecks(10, "h") == {0: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 1: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 2: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 3: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 4: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 5: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 6: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 7: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 8: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 9: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 10: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 11: [], 12: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 13: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 14: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']}

print "crosschecks 7,v"
assert alg.crosschecks(7, "v") == {0: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 1: [], 2: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 3: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 4: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 5: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 6: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 7: [], 8: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 9: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 10: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 11: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 12: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 13: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 14: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']}
print "--------------------"

alg.rack = ["O", "T", "A"]
(TopNode, trace) = alg.trie._get_node("")
#alg.ExtendRight("", TopNode, (10,11), (10,11), "h")

alg.ExtendRight("", TopNode, (7,7), (7,7), "v")
l1=len(alg.LegalMoves)
alg.ExtendLeft("", TopNode, 0, (7,7), (7,7), 'v')
l2=len(alg.LegalMoves)
#make sure an extendLeft with no free tiles to the left equals a call to extend right
assert l1 == l2
alg.ExtendLeft("", TopNode, len(alg.rack), (7,7), (7,7), 'v')
l3 = len(alg.LegalMoves)
#make sude considering left tiles leads to more moves
assert l3 > l2
print "moves",alg.LegalMoves

#pdb.set_trace()
