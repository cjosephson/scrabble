import treeBuilder
import board
import pygtrie
import pdb

##################################
# Appel Jaconson Algorithm Bits
################################

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
				self.crosscheckList[row][col] = set(alphabet)

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

        #########################################################
        # generate moves -> 
        # generateMoves(self, rack) where rack is list of tiles = characters
        # return (string, v/h, starting[row][col],
        # what characters were used from the rack)
        ##########################################################
        def generateMoves(self, rack):
                # compute anchors and crosschecks
                anchors = self.findAnchors()
                h = {}
                v = {}
                for (r,c, o) in anchors:
                        if r not in h:
                                h[r] = True
                        if c not in v:
                                v[c] = True
                for r in h.iterkeys():
                        self.crosschecks(r,'h')
                for c in v.iterkeys():
                        self.crosschecks(c, 'r')
                self.rack = rack
                print "rac'",self.rack
                #clear legal moves
                self.LegalMoves = set()
                print "LegalMoves",self.LegalMoves
                (TopNode, trace) = self.trie._get_node("")
                for (r,c,o) in anchors:
                        if o == 'h':
                                #calculate blank tiles to the left:
                                #print "r,c",r,c
                                brow = self.board.getRow(r)
                                #print "brow",brow
                                prefix = [b[0] for b in brow[:c+1]]
                                print "AnchorH",(r,c),(r,c+1)
                                if r == 0:
                                        print "prefix",prefix
                                i = len(prefix)-1
                                lengthH = 0
                                while True:
                                        if lengthH < 7 and lengthH < len(prefix) and prefix[i] == ' ':
                                                lengthH +=1
                                                i -= 1
                                        else: break
                                #print "lengthH",lengthH
                                #print "prefix",prefix
                                
                                self.ExtendLeft("", TopNode, lengthH,
                                                (r,c), (r,c), 'h')
                        elif o == 'v':
                                #calculate blank tiles above
                                bcol = self.board.getCol(c)
                                prefix = [b[0] for b in bcol[:r+1]]
                                i = len(prefix)-1
                                lengthV = 0
                                print "AnchorV",(r,c),(r,c)
                                while True:
                                        if lengthV < 7 and lengthV < len(prefix) and prefix[i] == ' ':
                                                lengthV +=1
                                                i -= 1
                                        else: break
                                #TODO: fix how extendL/R don't actually take
                                #in the anchor square
                                self.ExtendLeft("", TopNode, lengthV,
                                                (r+1,c), (r+1,c), 'v')
            
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
			        self.crosscheckList[row][i] = set(self.crosscheckList[row][i]).intersection(letterList)

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
				self.crosscheckList[i][row] = set(self.crosscheckList[i][row]).intersection(letterList)
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
						anchorList.append((i,j, 'h'))
				if (colString[j] == " " and colString[j+1] != " "):
					if (j,i) not in anchorList:
						anchorList.append((j,i, 'v'))
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
                # bounds check for square
                if row >= len(self.board.board) or col >= len(self.board.board):
                        return
                
                # breaking abstraction barriers ROFL
		squareVal = self.board.board[row][col][0]
		#print PartialWord
		#print "edges", edges
		#print square

		if orientation == "h": nextSquare = (row, col+1)
		if orientation == "v": nextSquare = (row+1, col)
		#print nextSquare
		if squareVal == " ":
			if type(node.value) is not type(_SENTINEL):
                                #validate
                                print PartialWord, startSquare, orientation
                                #pdb.set_trace()
                                assert self.board.valid(PartialWord, startSquare,
                                                        orientation)
				self.LegalMoves.add((PartialWord, startSquare,
                                                     orientation))
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
                row, col = startSquare
                rightSquare = ((row, col+1) if orientation == "h"
                              else (row+1, col))
                self.ExtendRight(PartialWord, node, rightSquare,
                                 rightSquare, orientation)
                                        
                if limit > 0:
                        self.crosschecks(row, orientation)
                        edges = node.children.keys()
                        for l in edges:
                                if l in self.rack:
                                        #pdb.set_trace()
                                        print "rack",self.rack
                                        print "l",l
                                        print "ccl",self.crosscheckList[row][col]
                                        if l in self.crosscheckList[row][col]:
                                                print "part",PartialWord
					        self.rack.remove(l)
					        newNode = node.children[l]
					        self.ExtendLeft(PartialWord+l,
                                                                newNode, limit-1,
                                                                anchorSquare,
                                                                nextSquare,
                                                                orientation)
					        self.rack.append(l)