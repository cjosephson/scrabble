import board, oracle, baseline

boards = []

b = board.Board()
boards.append(b)




####################################
b.insertWord("HELD", (3,7), 'h')
b.insertWord("EPHA", (1,7), 'v')
print b
print b.score('GOAT', (4,5), 'h')

b=board.Board()
b.insertWord('AVOWS', (4,7), 'v')
b.insertWord('WAILS', (7,7), 'h')
b.insertWord('WAGES', (3,11), 'v')
print b

b=board.Board()
b.insertWord('MURA', (11,1), 'h')
print b.valid('MULE', (11,1), 'v')
b.insertWord('MULE', (11,1), 'v')
print b

b=board.Board()
b.insertWord('TINE', (10,12), 'v')
print b.humanValid('TAM', (10,12), 'h', ['L', 'M', 'J', 'D', 'W', 'E', 'D'])
b.insertWord('TAM', (10,12), 'h')
print b 

#TODO: fix
b=board.Board()
b.insertWord('POPE', (1,10), 'h')
b.insertWord('TEE', (0,13), 'v')
b.insertWord('TA', (0,13), 'h')
print b.humanValid('POPES', (1,10), 'h', ['U', 'C', 'I', 'L', 'A', 'A', 'S'])
b.insertWord('POPES', (1,10), 'h')
print b


assert b.score("WELT", (10,10), 'h') ==  b.insertWord("WELT", (10,10), 'h')

b=board.Board()
b.insertWord('MURA', (0,0), 'h')
print b.valid('MULE', (0,0), 'v')
b.insertWord('MULE', (0,0), 'v')
print b

b=board.Board()
b.insertWord('AVOW', (11,10), 'v')
b.insertWord('WAILS', (14,10), 'h')
b.insertWord('WAGES', (10,14), 'v')
print b

b=board.Board()
b.insertWord('AVOW', (10,10), 'v')
b.insertWord('WAILS', (13,10), 'h')
b.insertWord('WAGES', (9,14), 'v')
print b.score('ET', (14,11), 'h')
b.insertWord('ET', (14,11), 'h' )
print b
#TODO: test cases all corners of the board 
	


#####################################
# test score function
#####################################
#b.insertWord("UNIVERSITY", (6,3), 'h', debug=True)
#print b
#print "here"
#b.insertWord("TEST", (7,7), "h")
#print b.score("TEST", (0,14), "h") #-1 
#print b.score("TEST", (0,0), "h") 
#print b.score("TEST", (10,11), "h") #??
#print b.score("TEST", (0,11), "h") 
#print b.score("TEST", (14,11), "h") 
#print b.score("TEST", (10,12), "h") #-1
#b.insertWord("TEST", (11,12), "h") #-1
#print b
#print b.score("TEST", (0,14), "v") 
#print b.score("TEST", (0,0), "v") 
#print b.score("TEST", (10,11), "v") #??
#print b.score("TEST", (0,11), "v") 
#print b.score("TEST", (14,11), "v") #-1
#print b.score("TEST", (10,12), "v") 
#print b.score("TEST", (7,6), "v") #-1
#print b.score("TEST", (12,0), "v") #-1
#b.insertWord("TEST", (14,0), "h") 
#print b
#print b.score("TEST", (11,0), "v") #-1)
#b.insertWord("UNIVERSITY", (7,3), 'h', debug=True) 
#b.insertWord("AH", (4,4), 'v', debug=True)
#b.insertWord("SKATE", (7,7), 'h')
#b.insertWord("WET", (5,10), 'v')
#b.insertWord("SUN", (3,5), 'h')
#print b.score("MEN", (1,7), 'v')


#########################################
# test some stuff
###########################################
'''print "Testing board verification function..."
print "score('TREE',(7,11), 'v') =? 4"
assert b.score('TREE',(7,11), 'v') == 4
print "score('TREEHOUSES',(7,11), 'v') =? -1"
assert b.score('TREEHOUSES',(7,11), 'v') == -1
print "score('TREE',(5,4), 'h') =? 6"
assert b.score('TREE',(5,4), 'h') == 6
print "score('TREEHOUSES',(5,4), 'h') =? 19"
assert b.score('TREEHOUSES',(5,4), 'h') == 19
print "score('ACTION',(6,4), 'h') =? -1"
assert b.score('ACTION',(6,4), 'h') == -1
print "score('INTEGER',(7,5), 'v') =? -1"
assert b.score('INTEGER',(7,5), 'v') == -1
print "score('RAZZMATAZZES',(10,4), 'h') =? -1"
assert b.score('RAZZMATAZZES',(10,4), 'h') == -1

b = board.Board()
b.insertWord("PET", (7,7), 'h')
b.insertWord("WET", (6,8), 'v')
assert b.insertWord("AP", (7,8), 'v') == -1
print b'''

# #####################################################
# # Test Board #2
# #####################################################
'''
b2 = board.Board()
boards.append(b2)
b2.insertWord("HELLO", (7,4), 'h', debug=True)
b2.insertWord("WORLD", (6,8), 'v', debug=True) 
print b2
'''
# # #################################################
# # # Test Board #3
# # #################################################
# b3 = board.Board()
# boards.append(b3)

# b3.insertWord("RAVE", (5,7), 'v')
# b3.insertWord("SPARROW", (6,5), 'h', debug=True) 
# #print b3

# # 			
# # # Test Board #4
# # ################################################
# b4 = board.Board()
# boards.append(b4)

# b4.insertWord("PARTY", (7, 7), 'h', debug=True)
# b4.insertWord("PLATE", (7,7), 'v', debug=True)
# b4.insertWord("RAINBOW", (9,6), 'h',debug=True)
# b4.insertWord("TEA", (11, 6), 'h', debug=True)
# #print b4

# # ################################################
# # # Test Board #5
# # ################################################
# b5 = board.Board()
# boards.append(b)

# b5.insertWord("WORD", (7,7), 'v', debug=True)
# b5.insertWord("SCRABBLE", (9, 5), 'h', debug=True)
# b5.insertWord("GAME", (6, 12), 'v', debug=True)
# #print b5

# # ################################################
# # # Test Board #6
# # ################################################
# b6 = board.Board()
# boards.append(b)

# b6.insertWord("WINNER", (7,3), 'h', debug=True)
# b6.insertWord("SWEET", (6, 3), 'v', debug=True)
# b6.insertWord("FUN", (5, 5), 'v', debug=True)
# b6.insertWord("FRIENDS", (5,5), 'h', debug=True)
# b6.insertWord("GAME", (2,8), 'v', debug=True)
# b6.insertWord("TOGA", (2,6), 'h', debug=True)
# #print b6

# # ################################################
# # # Test Board #7
# # ################################################
# b7 = board.Board()
# boards.append(b7)

# b7.insertWord("ARE",(7,6),'h',debug=True)
# b7.insertWord("YOU",(11,7),'h',debug=True)
# b7.insertWord("READY",(7,7),'v',debug=True)
# #print b7

# # ################################################
# # # Test Board #8
# # ################################################
# b8 = board.Board()
# boards.append(b8)

# b8.insertWord("BACK", (6,5),'h', debug=True)
# b8.insertWord("TO",(8,6),'h', debug=True)
# b8.insertWord("SCHOOL",(5, 7),'v', debug=True)
# b8.insertWord("LEARN",(10,7),'h', debug=True)
# b8.insertWord("MATH",(9,9), 'v', debug=True)
# #print b8

# # ################################################
# # # Test Board #9
# # ################################################
# b9 = board.Board()
# boards.append(b9)

# b9.insertWord("TABLESPOON",(7,4),'h',debug=True)
# b9.insertWord("ROCKS",(6, 12),'v',debug=True)
# #print b9

# # ################################################
# # # Test Board #A
# # ################################################
# bA = board.Board()
# boards.append(bA)

# bA.insertWord("DANCE",(0,4),'v',debug=True)
# bA.insertWord("TRAVEL",(0,9),'h',debug=True)
# bA.insertWord("READ",(0,10),'v',debug=True)
# bA.insertWord("DRINK",(2,1), 'h',debug=True)
# bA.insertWord("AYOO",(2,10),'h',debug=True)
# bA.insertWord("BRIDE",(3,7),'h',debug=True)
# bA.insertWord("BIRTHDAY",(3,7),'v',debug=True)
# bA.insertWord("BLUE",(4,1),'h',debug=True)
# bA.insertWord("BEATLES",(4,1), 'v',debug=True)
# bA.insertWord("QUIZ",(5,11),'v',debug=True)
# bA.insertWord("WAFER",(6,0),'h',debug=True)
# bA.insertWord("CHANTING",(7,6),'h',debug=True)
# bA.insertWord("NOTE",(7,9),'v',debug=True)
# bA.insertWord("FEAST",(9,0),'h',debug=True)
# bA.insertWord("SHOWER",(9,3),'v',debug=True)
# bA.insertWord("HAPPY",(10,3),'h',debug=True)
# bA.insertWord("SWIM",(12,2), 'h',debug=True)
# bA.insertWord("ENJOY", (13,5), 'h',debug=True)
# #print bA


# # ################################################
# # # Test Board #N, empty board
# # ################################################
# bN = board.Board()
# boards.append(bN)
# #print bN

# # for i in boards:
# #     print i
# #     print "Calculating baseline..."
# #     ba = baseline.Baseline(i)
# #     ba.move()

# #     print "Calculating oracle (takes a while...)"
# #     o = oracle.Oracle(i)
# #     o.move()
