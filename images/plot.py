import matplotlib.pyplot as plt
points = []
scores =  {0: (198, 343), 1: (236, 457), 2: (315, 243), 3: (258, 247), 4: (251, 202)}
for p in scores.itervalues(): points.append(p)
scores = {0: (233, 234),  2: (247, 333), 4: (209, 254)}
for p in scores.itervalues(): points.append(p)
scores = {0: (289, 289), 1: (282, 297), 2: (226, 278)}
for p in scores.itervalues(): points.append(p)
scores = {0: (196, 311), 2: (188, 413), 3: (231, 298), 4: (234, 187)}
for p in scores.itervalues(): points.append(p)
scores = {0: (237, 232), 1: (235, 238), 2: (254, 410), 3: (297, 401), 4: (253, 405), 5: (303, 297), 6: (169, 272), 7: (242, 236), 9: (233, 396)}
for p in scores.itervalues(): points.append(p)
scores = {0: (277, 255), 1: (306, 258), 2: (226, 267), 3: (285, 245), 4: (287, 302), 5: (216, 260), 6: (178, 384), 7: (258, 198), 8: (177, 232), 9: (266, 331)}
for p in scores.itervalues(): points.append(p)
scores = {0: (309, 346), 1: (250, 349), 2: (345, 206), 3: (251, 176), 4: (244, 181), 6: (212, 455), 7: (251, 342), 8: (269, 402), 9: (229, 220)}
for p in scores.itervalues(): points.append(p)
scores = {0: (232, 313), 1: (170, 293), 2: (269, 447),  4: (221, 289), 5: (242, 340), 6: (362, 260), 7: (232, 283), 8: (223, 264), 9: (241, 385)}
for p in scores.itervalues(): points.append(p)
scores = {0: (184, 215), 1: (221, 156), 2: (300, 410), 3: (284, 366), 4: (165, 305), 5: (235, 256), 6: (237, 193), 7: (212, 450), 8: (243, 263), 9: (273, 283)}
for p in scores.itervalues(): points.append(p)
scores = {0: (197, 361), 1: (190, 244), 2: (334, 246), 3: (231, 342), 4: (218, 368), 5: (300, 328), 6: (298, 243), 7: (224, 294), 8: (227, 377), 9: (224, 370)}
for p in scores.itervalues(): points.append(p)
scores = {0: (215, 218), 1: (259, 178), 2: (308, 396), 3: (286, 203), 5: (274, 217), 6: (257, 366), 7: (258, 433), 8: (187, 256), 9: (244, 223)}
for p in scores.itervalues(): points.append(p)
scores =  {0: (273, 398), 1: (298, 201), 2: (326, 282), 3: (319, 280), 4: (235, 386), 5: (241, 358), 6: (231, 220), 7: (227, 269), 8: (199, 249), 9: (304, 410), 10: (196, 204),  13: (239, 302), 14: (246, 182), 15: (157, 243)}
for p in scores.itervalues(): points.append(p)
scores = {0: (300, 300), 1: (278, 431), 3: (292, 262), 4: (293, 349), 5: (255, 353)}
for p in scores.itervalues(): points.append(p)

print "points",points
deltas = []
ratios = []
cs221 = 0
quackle = 0
numGames = len(points)
for p in points:
    quackle += p[1]
    cs221 += p[0]
    ratios.append(p[1]/float(p[0]))
    deltas.append(p[1] - p[0])
deltas = sorted(deltas)
ratios = sorted(ratios)
winRate = 0
smashedRate = 0
smashingRate = 0
for g in ratios:
    if g < 0.5:
        smashingRate += 1
    if g < 1:
        winRate += 1
    if g >= 2:
        smashedRate +=1
winRate = winRate/float(numGames)
smashedRate = smashedRate/float(numGames)
smashingRate = smashingRate/float(numGames)
print "deltas",deltas
print "num games", numGames
print "quackle avg",quackle/float(numGames)
print "cs221 avg",cs221/float(numGames)
print "avg delta",sum(deltas)/float(numGames)
print "win rate",winRate
print "smashed rate",smashedRate
print "smashing rate",smashingRate
print "best ratio", 1.0/ratios[0]
print "ratios",ratios
plt.bar(range(numGames), deltas, color="yellow")
#plt.plot([i for i in xrange(len(us))], us, label="cs221", marker = '.')
#plt.plot([i for i in xrange(len(quackle))], quackle, label="quackle", marker = '.')
plt.title('Quackle vs cs221 Score Differentials')
plt.xlabel("game number")
#plt.ylim([0, 600])
plt.ylabel("Quackle minus cs221 Score ")
plt.legend()
plt.show()
