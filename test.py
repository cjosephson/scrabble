import board, oracle, baseline

boards = []

b = board.Board()
boards.append(b)

#TODO: use addWord function
b.insert('S', (4,4))
b.insert('T', (5,4))
b.insert('A', (6,4))

b.insert('U',(7, 3))
b.insert('N',(7, 4))
b.insert('I',(7, 5))
b.insert('V',(7, 6))
b.insert('E',(7, 7))
b.insert('R',(7, 8))
b.insert('S',(7, 9))
b.insert('I',(7, 10))
b.insert('T',(7, 11))
b.insert('Y',(7, 12))

b.insert('F', (8,4))
b.insert('O', (9,4))
b.insert('R', (10,4))
b.insert('D', (11,4))
print b
# print "Testing board verification function..."
# print "score('TREEHOUSES',(11,7), 'v') =? -1"
# assert b.score('TREEHOUSES',(11,7), 'v') == -1
# print "score('TREE',(11,7), 'v') =? -1"
# assert b.score('TREE',(11,7), 'v') == 4
# print "score('TREE',(4,5), 'h')"
# assert b.score('TREE',(4,5), 'h') == 4
# print "score('TREEHOUSES',(4,5), 'h')"
# assert b.score('TREEHOUSES',(4,5), 'h') == -1
# print "score('ACTION',(4,6), 'h')"
# assert b.score('ACTION',(4,6), 'h') == -1
# print "score('INTEGER',(5,7), 'v')"
# assert b.score('INTEGER',(5,7), 'v') == -1
# print "score('RAZZMATAZZES',(4,10), 'h')"
# assert b.score('RAZZMATAZZES',(4,10), 'h') == -1

# #####################################################
# # Test Board #2
# #####################################################

# b2 = board.Board()
# boards.append(b2)

# b2.board[7] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('W'),(' '),(' '),(' '),(' ')]
# b2.board[6] = [(' '),(' '),(' '),(' '),(' '),(' '),('H'),('E'),('L'),('L'),('O'),(' '),(' '),(' '),(' ')]
# b2.board[5] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('R'),(' '),(' '),(' '),(' ')]
# b2.board[4] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('L'),(' '),(' '),(' '),(' ')]
# b2.board[3] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('D'),(' '),(' '),(' '),(' ')]

# #################################################
# # Test Board #3
# #################################################
# b3 = board.Board()
# boards.append(b3)

# b3.board[7] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('R'),(' '),(' '),(' '),(' '),(' '),(' ')]
# b3.board[6] = [(' '),(' '),(' '),(' '),(' '),(' '),('S'),('P'),('A'),('R'),('R'),('O'),('W'),(' '),(' ')]
# b3.board[5] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('V'),(' '),(' '),(' '),('I'),(' '),(' ')]
# b3.board[4] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('E'),(' '),(' '),(' '),('N'),(' '),(' ')]
# b3.board[3] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('G'),(' '),(' ')]

# ################################################
# # Test Board #4
# ################################################
# b4 = board.Board()
# boards.append(b4)

# b4.board[7] = [(' '),(' '),(' '),(' '),(' '),(' '),('P'),('A'),('R'),('T'),('Y'),(' '),(' '),(' '),(' ')]
# b4.board[6] = [(' '),(' '),(' '),(' '),(' '),(' '),('L'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b4.board[5] = [(' '),(' '),(' '),(' '),(' '),('R'),('A'),('I'),('N'),('B'),('O'),('W'),(' '),(' '),(' ')]
# b4.board[4] = [(' '),(' '),(' '),(' '),(' '),(' '),('T'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b4.board[3] = [(' '),(' '),(' '),(' '),(' '),('T'),('E'),('A'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]

# ################################################
# # Test Board #5
# ################################################
# b5 = board.Board()
# boards.append(b)

# b5.board[9] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b5.board[8] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('G'),(' '),(' '),(' ')]
# b5.board[7] = [(' '),(' '),(' '),(' '),(' '),(' '),('W'),(' '),(' '),(' '),(' '),('A'),(' '),(' '),(' ')]
# b5.board[6] = [(' '),(' '),(' '),(' '),(' '),(' '),('O'),(' '),(' '),(' '),(' '),('M'),(' '),(' '),(' ')]
# b5.board[5] = [(' '),(' '),(' '),(' '),('S'),('C'),('R'),('A'),('B'),('B'),('L'),('E'),(' '),(' '),(' ')]
# b5.board[4] = [(' '),(' '),(' '),(' '),(' '),(' '),('D'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b5.board[3] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b5.board[2] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]

# ################################################
# # Test Board #6
# ################################################
# b6 = board.Board()
# boards.append(b)

# b6.board[14] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[13] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[12] = [(' '),(' '),(' '),(' '),(' '),('T'),('O'),('G'),('A'),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[11] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),('A'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[10] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),('M'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[9]  = [(' '),(' '),(' '),(' '),('F'),('R'),('I'),('E'),('N'),('S'),('S'),(' '),(' '),(' '),(' ')]
# b6.board[8]  = [(' '),(' '),('S'),(' '),('U'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[7]  = [(' '),(' '),('W'),('I'),('N'),('N'),('E'),('R'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[6]  = [(' '),(' '),('E'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[5]  = [(' '),(' '),('E'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[4]  = [(' '),(' '),('T'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[3]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[2]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[1]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b6.board[0]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]


# ################################################
# # Test Board #7
# ################################################
# b7 = board.Board()
# boards.append(b7)

# b7.board[14] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[13] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[12] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[11] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[10] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[9]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[8]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[7]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[6]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),('A'),('R'),('E'),(' '),(' '),(' '),(' '),(' ')]
# b7.board[5]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('E'),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[4]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('A'),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[3]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('D'),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[2]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('Y'),('O'),('U'),(' '),(' '),(' '),(' ')]
# b7.board[1]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b7.board[0]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]

# ################################################
# # Test Board #8
# ################################################
# b8 = board.Board()
# boards.append(b8)

# b8.board[14] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[13] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[12] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[11] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[10] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[9]  = [(' '),(' '),(' '),(' '),(' '),('S'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[8]  = [(' '),(' '),(' '),('B'),('A'),('C'),('K'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[7]  = [(' '),(' '),(' '),(' '),(' '),('H'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[6]  = [(' '),(' '),(' '),(' '),('T'),('O'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[5]  = [(' '),(' '),(' '),(' '),(' '),('O'),(' '),('M'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[4]  = [(' '),(' '),(' '),(' '),(' '),('L'),('E'),('A'),('R'),('N'),(' '),(' '),(' '),(' '),(' ')]
# b8.board[3]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),('T'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[2]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),('H'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[1]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b8.board[0]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]

# ################################################
# # Test Board #9
# ################################################
# b9 = board.Board()
# boards.append(b9)

# b9.board[14] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[13] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[12] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[11] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[10] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[9]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[8]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('R'),(' '),(' '),(' ')]
# b9.board[7]  = [(' '),(' '),(' '),('T'),('A'),('B'),('L'),('E'),('S'),('P'),('O'),('O'),('N'),(' '),(' ')]
# b9.board[6]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('C'),(' '),(' '),(' ')]
# b9.board[5]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('K'),(' '),(' '),(' ')]
# b9.board[4]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),('S'),(' '),(' '),(' ')]
# b9.board[3]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[2]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[1]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# b9.board[0]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]


# ################################################
# # Test Board #A
# ################################################
# bA = board.Board()
# boards.append(bA)

# bA.board[14] = [(' '),(' '),(' '),(' '),('D'),(' '),(' '),(' '),(' '),('T'),('R'),('A'),('V'),('E'),('L')]
# bA.board[13] = [(' '),(' '),(' '),(' '),('A'),(' '),(' '),(' '),(' '),(' '),('E'),(' '),(' '),(' '),(' ')]
# bA.board[12] = [(' '),('D'),('R'),('I'),('N'),('K'),(' '),(' '),(' '),(' '),('A'),('Y'),('O'),('U'),(' ')]
# bA.board[11] = [(' '),(' '),(' '),(' '),('C'),(' '),(' '),('B'),('R'),('I'),('D'),('E'),(' '),(' '),(' ')]
# bA.board[10] = [(' '),('B'),('L'),('U'),('E'),(' '),(' '),('I'),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bA.board[9]  = [(' '),('E'),(' '),(' '),(' '),(' '),(' '),('R'),(' '),(' '),(' '),('Q'),(' '),(' '),(' ')]
# bA.board[8]  = [('W'),('A'),('F'),('E'),('R'),(' '),(' '),('T'),(' '),(' '),(' '),('U'),(' '),(' '),(' ')]
# bA.board[7]  = [(' '),('T'),(' '),(' '),(' '),(' '),('C'),('H'),('A'),('N'),('T'),('I'),('N'),('G'),(' ')]
# bA.board[6]  = [(' '),('L'),(' '),(' '),(' '),(' '),(' '),('D'),(' '),('O'),(' '),('Z'),(' '),(' '),(' ')]
# bA.board[5]  = [('F'),('E'),('A'),('S'),('T'),(' '),(' '),('A'),(' '),('T'),(' '),(' '),(' '),(' '),(' ')]
# bA.board[4]  = [(' '),('S'),(' '),('H'),('A'),('P'),('P'),('Y'),(' '),('E'),(' '),(' '),(' '),(' '),(' ')]
# bA.board[3]  = [(' '),(' '),(' '),('O'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bA.board[2]  = [(' '),(' '),('S'),('W'),('I'),('M'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bA.board[1]  = [(' '),(' '),(' '),('E'),(' '),('E'),('N'),('J'),('O'),('Y'),(' '),(' '),(' '),(' '),(' ')]
# bA.board[0]  = [(' '),(' '),(' '),('R'),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]

# ################################################
# # Test Board #N, empty board
# ################################################
# bN = board.Board()
# boards.append(bN)

# bN.board[14] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[13] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[12] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[11] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[10] = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[9]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[8]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[7]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[6]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[5]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[4]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[3]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[2]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[1]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]
# bN.board[0]  = [(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' '),(' ')]

# for i in boards:
#     print "Calculating baseline..."
#     ba = baseline.Baseline(i)
#     ba.baselineMove()

#     print "Calculating oracle (takes a while...)"
#     o = oracle.Oracle(i)
#     o.OracleMove()
