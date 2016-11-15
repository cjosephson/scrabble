import random
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
    def getLetter(self):
	#grab a random number out of the bag
	i = random.randint(0, len(self.letters)-1)
	result = self.letters.pop(i)
	return result
        

