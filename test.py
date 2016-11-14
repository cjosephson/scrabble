import board, oracle, baseline

boards = []

b = board.Board()
boards.append(b)

b.insertWord("UNIVERSITY", (7,3), 'h', debug=True) 
b.insertWord("STANFORD", (4,4), 'v', debug=True)

print b
print "Testing board verification function..."
print "score('TREE',(11,7), 'v') =? 4"
assert b.score('TREE',(11,7), 'v') == 4
print "score('TREEHOUSES',(11,7), 'v') =? -1"
assert b.score('TREEHOUSES',(11,7), 'v') == -1
print "score('TREE',(4,5), 'h') =? 6"
assert b.score('TREE',(4,5), 'h') == 6
print "score('TREEHOUSES',(4,5), 'h') =? 19"
assert b.score('TREEHOUSES',(4,5), 'h') == 19
print "score('ACTION',(4,6), 'h') =? -1"
assert b.score('ACTION',(4,6), 'h') == -1
print "score('INTEGER',(5,7), 'v') =? -1"
assert b.score('INTEGER',(5,7), 'v') == -1
print "score('RAZZMATAZZES',(4,10), 'h') =? -1"
assert b.score('RAZZMATAZZES',(4,10), 'h') == -1

# #####################################################
# # Test Board #2
# #####################################################

b2 = board.Board()
boards.append(b2)
b2.insertWord("HELLO", (7,4), 'h', debug=True)
b2.insertWord("WORLD", (6,8), 'v', debug=True) 
print b2

# #################################################
# # Test Board #3
# #################################################
b3 = board.Board()
boards.append(b3)

b3.insertWord("RAVE", (5,7), 'v')
b3.insertWord("SPARROW", (6,5), 'h', debug=True) 
print b3

# ################################################
# # Test Board #4
# ################################################
b4 = board.Board()
boards.append(b4)

b4.insertWord("PARTY", (7, 7), 'h', debug=True)
b4.insertWord("PLATE", (7,7), 'v', debug=True)
b4.insertWord("RAINBOW", (9,6), 'h',debug=True)
b4.insertWord("TEA", (11, 6), 'h', debug=True)
print b4

# ################################################
# # Test Board #5
# ################################################
b5 = board.Board()
boards.append(b)

b5.insertWord("WORD", (7,7), 'v', debug=True)
b5.insertWord("SCRABBLE", (9, 5), 'h', debug=True)
b5.insertWord("GAME", (6, 12), 'v', debug=True)
print b5

# ################################################
# # Test Board #6
# ################################################
b6 = board.Board()
boards.append(b)

b6.insertWord("WINNER", (7,3), 'h', debug=True)
b6.insertWord("SWEET", (6, 3), 'v', debug=True)
b6.insertWord("FUN", (5, 5), 'v', debug=True)
b6.insertWord("FRIENDS", (5,5), 'h', debug=True)
b6.insertWord("GAME", (2,8), 'v', debug=True)
b6.insertWord("TOGA", (2,6), 'h', debug=True)
print b6

# ################################################
# # Test Board #7
# ################################################
b7 = board.Board()
boards.append(b7)

b7.insertWord("ARE",(7,6),'h',debug=True)
b7.insertWord("YOU",(11,7),'h',debug=True)
b7.insertWord("READY",(7,7),'v',debug=True)
print b7

# ################################################
# # Test Board #8
# ################################################
b8 = board.Board()
boards.append(b8)

b8.insertWord("BACK", (6,5),'h', debug=True)
b8.insertWord("TO",(8,6),'h', debug=True)
b8.insertWord("SCHOOL",(5, 7),'v', debug=True)
b8.insertWord("LEARN",(10,7),'h', debug=True)
b8.insertWord("MATH",(9,9), 'v', debug=True)
print b8

# ################################################
# # Test Board #9
# ################################################
b9 = board.Board()
boards.append(b9)

b9.insertWord("TABLESPOON",(7,4),'h',debug=True)
b9.insertWord("ROCKS",(6, 12),'v',debug=True)
print b9

# ################################################
# # Test Board #A
# ################################################
bA = board.Board()
boards.append(bA)

bA.insertWord("DANCE",(0,4),'v',debug=True)
bA.insertWord("TRAVEL",(0,9),'h',debug=True)
bA.insertWord("READ",(0,10),'v',debug=True)
bA.insertWord("DRINK",(2,1), 'h',debug=True)
bA.insertWord("AYOO",(2,10),'h',debug=True)
bA.insertWord("BRIDE",(3,7),'h',debug=True)
bA.insertWord("BIRTHDAY",(3,7),'v',debug=True)
bA.insertWord("BLUE",(4,1),'h',debug=True)
bA.insertWord("BEATLES",(4,1), 'v',debug=True)
bA.insertWord("QUIZ",(5,11),'v',debug=True)
bA.insertWord("WAFER",(6,0),'h',debug=True)
bA.insertWord("CHANTING",(7,6),'h',debug=True)
bA.insertWord("NOTE",(7,9),'v',debug=True)
bA.insertWord("FEAST",(9,0),'h',debug=True)
bA.insertWord("SHOWER",(9,3),'v',debug=True)
bA.insertWord("HAPPY",(10,3),'h',debug=True)
bA.insertWord("SWIM",(12,2), 'h',debug=True)
bA.insertWord("ENJOY", (13,5), 'h',debug=True)
print bA


# ################################################
# # Test Board #N, empty board
# ################################################
bN = board.Board()
boards.append(bN)
print bN

for i in boards:
    print "Calculating baseline..."
    ba = baseline.Baseline(i)
    ba.baselineMove()

    print "Calculating oracle (takes a while...)"
    o = oracle.Oracle(i)
    o.OracleMove()
