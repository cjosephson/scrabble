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
                self.sortedDict = {}
                for k in board.dictionary:
                        s = ''.join(sorted(k))
                        if s not in self.sortedDict:
                                self.sortedDict[s] = [k]
                        else:
                                self.sortedDict[s] += k
		self.bag = LetterBag() #later we should move this
		self.tiles = [] # list of tiles current in posession 

		# get first 7 tiles
                for i in xrange(7):
                        self.tiles.append(self.bag.getLetter())

	#####################################################
	# Score: 
	# Returns the base score of a word (no multipliers)
	# currently assumes no multiplier tiles for discarding
	# keys
	#####################################################		
	def move(self):
		#make a new dict of sortedWords->realWords, sort our
		#letters plus tiles, then remove a subset until a
		#valid match is found
                score = -1
                word = ''
		#find any possible move and do it
		for c in xrange(15):
                        #print "-----------------------------------------"
			col = self.board.getCol(c)
                        colStr = ''.join(''.join([i[0] for i in col]).split())
                        #print colStr
                        if colStr == '':
                                continue
                        
                        #search loop
                        for  i in xrange(222):
                                # choose a random subset from our bag
                                num = random.randint(1, len(self.tiles))
                                subset = []
                                #choose num random tiles
                                for j in random.sample(xrange(7), num):
                                        subset.append(self.tiles[j])
                                #print "tiles",self.tiles
                                #print "subset",subset
                                #sortedLetters = ''.join(sorted(''.join(self.tiles) + colStr))
                                
                                #for each letter already on the board,
                                #try and form a word around it from
                                #our subset
                                for j in colStr:
                                        k = ''.join(sorted(''.join(subset)+colStr))
                                        if k not in self.sortedDict:
                                                continue
                                        #print "it's a word!",k
                                        #test for validity
                                        for y in xrange(15): #try all positions
                                                #(word, startPoint, orientation):
                                                score = self.board.score(k, (c,y), 'v')
					        #print "(%i, %i) score = % i"%(c,y,score)
                                                if score > 0:
                                                        word = k
                                                        print "BASELN: max word is %s with score %i at %s,%s"%(word,
                                                                                                               score,
                                                                                                               (c,y),
                                                                                                               'v') 
                                                        #remove used letters
                                                        print "score of word",self.board.insertWord(word, (c,y), 'v')
                                                        (self.tiles.remove(t) for t in subset)
                                                        (self.tiles.append(self.bag.getLetter()) for t in subset)
                                                        return score
                print "BASELINE found no word"
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
			
		#print len(self.letters), count
	def getLetter(self):
		#grab a random number out of the bag
		i = random.randint(0, len(self.letters)-1)
		result = self.letters.pop(i)
		return result



if __name__ == '__main__':
	bag = LetterBag()
