#import treeBuilder
import board
import pygtrie
import pdb
import copy 
import pickle
import letterbag
from operator import itemgetter
##################################
# Appel Jaconson Algorithm Bits
################################

_SENTINEL =  object()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',\
	    'H', 'I', 'J', 'K', 'L', 'M', 'N',\
	    'O', 'P', 'Q', 'R', 'S', 'T', 'U',\
	    'V', 'W', 'X', 'Y', 'Z']

def runSimulations(rack, word, loc, orientation, board, alg, depth = 2):
    scoreDiff = 0
    rack1 = rack
    numIters = 10
    tempBoard = copy.deepcopy(board)
    alg.board = tempBoard
   # alg = AJalgorithm(tempBoard)
    # start by assigning random
    for i in range(numIters):
        print '.',
        import sys
        sys.stdout.flush()
        simbag = letterbag.LetterBag()
        rack2 = []
        for l in range(7):
            rack2.append(simbag.getLetter())
        #print "Rack 1", rack1
        #print "Rack 2", rack2
        scoreDiff += simulation(rack1, rack2, word, loc, orientation, tempBoard, depth, alg)
    #average/weighted average of many simulations
    alg.board = board
    return scoreDiff/numIters

def simulation(rack1, rack2, word, loc, orientation, tempBoard, depth, alg): 
    #use a tempboard
    #print tempBoard
    #move1
    score1 = 0
    score2 = 0
    if depth > 2: 
        moveList = alg.generateMoves(rack1)
        if len(alg.LegalMoves) > 0:
            (word, loc, orientation, usedTiles, score) = max(alg.LegalMoves, key=itemgetter(4))
            score1 = tempBoard.insertWord(word, loc, orientation)
     #       print score1
    else:
        score1 = tempBoard.insertWord(word, loc, orientation)
      #  print score1

    #print tempBoard
    #move2
    moveList = alg.generateMoves(rack2)
    if len(alg.LegalMoves) > 0:
        (word, loc, orientation, usedTiles, score) = max(alg.LegalMoves, key=itemgetter(4))
        score2 = tempBoard.insertWord(word, loc, orientation)
     #   print score2
    #print tempBoard
    return score1-score2

class AJalgorithm:
	def __init__(self, board):
		self.board = board
		self.trie = pickle.load(open("trie.p", "rb"))
		self.LegalMoves = set() #list of legal moves. gets changed every time getMove is called
		self.rack = []
                self.origRack = []
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
                self.origRack = copy.deepcopy(rack)
                #print "rac'",self.rack
                #clear legal moves
                self.LegalMoves = set()
                #print "LegalMoves",self.LegalMoves
                (TopNode, trace) = self.trie._get_node("")
                for (r,c,o) in anchors:
                        if o == 'h':
                                #calculate blank tiles to the left:
                                #print "r,c",r,c
                                brow = self.board.getRow(r)
                                #print "brow",brow
                                prefix = [b[0] for b in brow[:c+1]]
                                #print "AnchorH",(r,c),(r,c+1)
                                #if r == 0: print "prefix",prefix
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
                                                (r,c+1), (r,c+1), 'h')
                        elif o == 'v':
                                #calculate blank tiles above
                                bcol = self.board.getCol(c)
                                prefix = [b[0] for b in bcol[:r+1]]
                                i = len(prefix)-1
                                lengthV = 0
                                #print "AnchorV",(r,c),(r+1,c)
                                while True:
                                        if lengthV < 7 and lengthV < len(prefix) and prefix[i] == ' ':
                                                lengthV +=1
                                                i -= 1
                                        else: break
                                #TODO: fix how extendL/R don't actually take
                                #in the anchor square
                                self.ExtendLeft("", TopNode, lengthV,
                                                (r+1,c), (r+1,c), 'v')
                        #TODO: remove moves that use no letters from the rack
                        remove = []
                        #print "PRE",self.LegalMoves
                        for m in self.LegalMoves:
                                if len(m[3]) == 0:
                                        remove.append(m)
                        #print "REMOVE",remove
                        for r in remove:
                                self.LegalMoves.remove(r)
            
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

        def rackdiff(self):
                used = ''
                for t in self.origRack:
                        if t not in self.rack:
                                used += t
                return used
        
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
                                #print PartialWord, startSquare, orientation
                                #pdb.set_trace()
                                
                                #assert self.board.valid(PartialWord, startSquare,
                                #                        orientation)
                                score = self.board.score(PartialWord, startSquare, orientation)
                                if score > -1:
				        self.LegalMoves.add((PartialWord, startSquare,
                                                             orientation, self.rackdiff(), score))
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
                if limit > 0:
                        row, col = startSquare
                        self.crosschecks(row, orientation)
                        self.ExtendRight(PartialWord, node, anchorSquare,
                                         startSquare, orientation)
                        nextSquare = ((row, col-1) if orientation == "h"
                                     else (row-1, col))
                
                        edges = node.children.keys()
                        for l in edges:
                                if l in self.rack:
                                        #pdb.set_trace()
                                        if l in self.crosscheckList[nextSquare[0]][nextSquare[1]]:
                                                #print "l",l
                                                #print "part",PartialWord
                                                #print "nextSquare",nextSquare
                                                #print "ccl",self.crosscheckList[nextSquare[0]][nextSquare[1]]
					        self.rack.remove(l)
					        newNode = node.children[l]
					        self.ExtendLeft(PartialWord+l,
                                                                newNode, limit-1,
                                                                anchorSquare,
                                                                nextSquare,
                                                                orientation)
					        self.rack.append(l)
