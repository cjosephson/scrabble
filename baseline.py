# CS221 Final Project
# Becca Greene & Colleen Josphson
import random, itertools

#####################################################
# Baseline: 
# lower bound metric on best possible move performance
# metric. Very lower. Slow AF 
#####################################################

class Baseline:
	def __init__(self, board):
		self.board = board
		self.bag = LetterBag() #later we should move this
		self.tiles = [] # list of tiles current in posession 

		# get first 7 tiles
		self.tiles.append(bag.getLetter())
		self.tiles.append(bag.getLetter())
		self.tiles.append(bag.getLetter())
		self.tiles.append(bag.getLetter())
		self.tiles.append(bag.getLetter())
		self.tiles.append(bag.getLetter())
		self.tiles.append(bag.getLetter())
	#####################################################
	# Score: 
	# Returns the base score of a word (no multipliers)
	# currently assumes no multiplier tiles for discarding
	# keys
	#####################################################		
	def baselineMove(self, board):
		
		#find any possible move and do it
		for col in range(15):
			vector = board.getCols(col)

			#vector to string
			vectorString = ""
			for c in vector:
				vectorString += c

			strList =- vectorString.split() 

			#make sure vector not empty
			if strList != []:
				for i in range(len(self.letters)):
					fexes = itertools.permutations()



		return None

class LetterBag:
	def __init__(self):
		self.letters = []
		count = 0
		#fill the bag with starting values
		for i in range(12):
			self.letters.append('E')
			if  i < 9: 
				self.letters.append('I')
			if i< 8: 
				self.letters.append('A')
			if i < 6:
				self.letters.append('N')
				self.letters.append('O')
				self.letters.append('R')
				self.letters.append('T')
			if i < 5:
				self.letters.append('W')
			if i < 4:
				self.letters.append('L')
				self.letters.append('S')
				self.letters.append('U')
				self.letters.append('D')
			if i < 3: 
				self.letters.append('G')
				self.letters.append('B')
				self.letters.append('C')
				self.letters.append('M')
				self.letters.append('P')
			if i < 2:
				self.letters.append('F')
				self.letters.append('H')
				self.letters.append('V')
				self.letters.append('Y')
				self.letters.append('K')
			if i < 1: 
				self.letters.append('J')
				self.letters.append('X')
				self.letters.append('Q')
				self.letters.append('Z')
			
		print len(self.letters), count
	def getLetter(self):
		#grab a random number out of the bag
		i = random.randint(0, len(self.letters))
		result = self.letters.pop(i)
		return result



if __name__ == '__main__':
	bag = LetterBag()