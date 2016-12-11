import random
from collections import defaultdict
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
        if self.size() > 1:
	    i = random.randint(0, len(self.letters)-1)
	    result = self.letters.pop(i)
        elif self.size() == 1:
            result = self.letters.pop()
        else:
            result = None
	return result

    def exchange(self, t):
        self.letters.append(t)
        return self.getLetter()
    
    def empty(self):
        return len(self.letters) == 0
	
    def putLetter(self, letter):
        self.letters.append(letter)

    def popLetter(self, letter):
        if letter in self.letters:
            self.letters.remove(letter)

    def size(self):
        return len(self.letters)

    def getProb(self, letter):
		#print self.letters
		#print self.letters.count(letter)
		return float(self.letters.count(letter)+1)/float(len(self.letters)+1)

    def __str__(self):
        d = {}#defaultdict(int)
        for l in self.letters:
            d[l] = 1 + d.get(l,0)# += 1
        return str(d)
        

