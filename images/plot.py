import matplotlib.pyplot as plt
points = []
scores = {0: (281, 416), 1: (257, 252), 2: (236, 624), 3: (452, 298), 4: (268, 498), 6: (276, 358), 7: (289, 463), 8: (285, 350), 9: (251, 530), 10: (287, 404), 11: (388, 313), 12: (292, 296), 13: (315, 423), 14: (242, 354), 15: (307, 435), 16: (263, 370), 17: (316, 406), 18: (220, 401), 19: (339, 352), 20: (331, 235), 21: (286, 257), 22: (279, 545), 23: (311, 389), 24: (332, 289), 25: (268, 330), 26: (279, 394), 27: (268, 286), 28: (332, 514), 29: (254, 405)}
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
