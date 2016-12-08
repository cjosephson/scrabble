import matplotlib.pyplot as plt
points = []
# vanilla AI, n=111
scores = {0: (261, 390), 1: (259, 348), 2: (326, 524), 3: (194, 442), 4: (242, 233), 5: (265, 202), 6: (296, 429), 7: (262, 328), 8: (243, 463), 9: (276, 354), 10: (264, 555), 11: (317, 483), 12: (278, 383), 13: (381, 428), 14: (310, 458), 15: (297, 514), 16: (206, 414), 17: (266, 141), 18: (288, 328), 19: (255, 495), 20: (252, 564), 21: (276, 358), 22: (232, 390), 23: (267, 396), 24: (290, 335), 25: (249, 528), 26: (274, 458), 27: (231, 444), 28: (230, 276), 29: (332, 394), 30: (271, 448), 31: (307, 273), 32: (230, 305), 33: (273, 545), 34: (329, 348), 35: (243, 471), 36: (242, 286), 37: (255, 344), 38: (262, 342), 39: (351, 408), 40: (238, 503), 41: (269, 336), 42: (310, 493), 43: (312, 577), 44: (312, 329), 45: (295, 400), 46: (238, 432), 47: (357, 424), 48: (322, 429), 49: (277, 381), 50: (320, 382), 51: (217, 505), 52: (308, 435), 53: (366, 230), 54: (252, 235), 55: (318, 309), 56: (258, 422), 57: (258, 317), 58: (251, 520), 59: (266, 444), 60: (242, 450), 61: (389, 389), 62: (314, 325), 63: (306, 438), 64: (206, 404), 65: (312, 534), 66: (245, 427), 67: (306, 402), 68: (304, 449), 69: (206, 346), 70: (280, 545), 71: (255, 223), 72: (348, 383), 73: (216, 264), 74: (309, 252), 75: (357, 432), 76: (326, 424), 77: (162, 575), 78: (262, 312), 79: (212, 456), 80: (238, 332), 81: (284, 382), 82: (192, 297), 83: (226, 494), 84: (334, 424), 85: (254, 633), 86: (265, 316), 87: (268, 496), 88: (272, 449), 89: (343, 321), 90: (314, 495), 91: (336, 321), 92: (257, 319), 93: (226, 352), 94: (302, 355), 95: (317, 269), 96: (285, 374), 97: (267, 280), 98: (266, 318), 99: (292, 366)}#, 100: (297, 404), 101: (221, 246), 102: (261, 406), 103: (191, 413), 104: (217, 354), 105: (249, 644), 106: (308, 549), 107: (305, 360), 108: (182, 380), 109: (257, 288), 110: (247, 382)}
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
