import os, random, operator, sys
from collections import Counter
import copy

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',\
	    'H', 'I', 'J', 'K', 'L', 'M', 'N',\
	    'O', 'P', 'Q', 'R', 'S', 'T', 'U',\
	    'V', 'W', 'X', 'Y', 'Z']

vowels = ['A','E','I','O','U','Y']

letterToPoints = {'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'Y':4, 'W':4,
                  'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10,'A':1, 'E':1, 'I':1, 'O':1, 'N':1, 
                  'R':1, 'T':1, 'L':1, 'S':1, 'U':1, }

letterMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
             0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O'}

# rack heuristics, no monte carlo
weightsA = {'GG': -4, 'AAA': 27, 'BB': -12, 'DD': 43, 'WW': 8, 'EEE': 436, 'L': -513, 'CC': -5, 'NNN': 30, 'NN': -22, 'VVV': -89, 'TT': -64, 'TTT': -168, 'AA': -7, 'EE': 81, 'GGG': -286, 'PPP': 187, 'CCC': -144, 'LLL': -147, 'III': 35, 'RRR': -52, 'A': 686, 'C': -278, 'B': 110, 'E': 842, 'D': 218, 'G': -189, 'F': 670, 'I': 264, 'H': -215, 'K': 592, 'J': -534, 'M': 529, 'vc_ratio': -225.33333333333334, 'O': 778, 'N': 410, 'Q': 326, 'P': 267, 'S': 161, 'R': -609, 'raw_score': 278471, 'T': -217, 'W': 372, 'V': -45, 'Y': -262, 'X': 144, 'Z': 91, 'DDD': 12, 'OO': -19, 'II': -63, 'WWW': -158, 'QU': -55, 'RR': -249, 'UUU': -665, 'OOO': 163, 'YYY': 61, 'SSS': 37, 'MMM': 88, 'UU': -133, 'KKK': 37, 'FFF': 16, 'U': -348, 'HHH': 62, 'BBB': 9, 'LL': -155}

# including MC (preliminary, 36 iterations to go)
weights_MC = {'AA': 27, 'AAA': 41, 'DD': -16, 'EE': -10, 'WW': -7, 'EEE': -27, 'CCC': -64, 'II': 52, 'NNN': -37, 'Z': -45, 'RR': 12, 'TTT': -169, 'CC': -33, 'GGG': -98, 'PPP': 1, 'LLL': -162, 'III': 112, 'RRR': -19, 'A': 101, 'C': -69, 'B': 94, 'E': 181, 'D': 127, 'G': 138, 'F': -29, 'I': 36, 'H': 121, 'K': -43, 'J': -185, 'M': 45, 'vc_ratio': 114.99999999999994, 'O': -61, 'L': -152, 'Q': 132, 'P': -252, 'S': -12, 'R': -56, 'raw_score': 32736, 'T': 157, 'W': 60, 'V': -16, 'Y': 42, 'X': 200, 'N': 184, 'DDD': 6, 'OO': 23, 'GG': -21, 'WWW': 25, 'mc_score': 1017.1007421851381, 'QU': -41, 'NN': 20, 'UUU': -23, 'OOO': 37, 'SSS': -12, 'MMM': 47, 'KKK': -21, 'U': 54, 'BBB': 5}

def featureExtractor(origRack, raw_score, mc_score=None):
    features = {}
    rack = copy.deepcopy(origRack)  
    # Features TODO:
    # -doubles/triples (done)
    # -'qu' (done)
    # -consonants to vowels ratio
    # -include scrabble letter value somehow? sum of tile values
    if ('Q' in rack) and ('U' in rack): features['QU'] = 1
    features['raw_score'] = raw_score
    def multiplier(c):
        return 1#letterToPoint[c]
    if mc_score:
        features['mc_score'] = mc_score
    for char in alphabet:
        c2 = char+char
        c3 = char+char+char
        if char in rack:
            rack.remove(char)
            if char in rack:
                rack.remove(char)
                if char in rack: 
                    features[c2] = 1*multiplier(char)
                else:
                    features[c3] = 1*multiplier(char)
            else:
                features[char] = 1*multiplier(char)
        v = 0
        c = 0
        for t in rack:
            if t in vowels: v += 1
            else: c += 1
        features['vc_ratio'] = (v+1)/(float(c)+1)
    return features

def dotProduct(d1, d2):
    """
    @param dict d1: a feature vector represented by a mapping from a feature (string) to a weight (float).
    @param dict d2: same as d1
    @return float: the dot product between d1 and d2
    """
    if len(d1) < len(d2):
        return dotProduct(d2, d1)
    else:
        return sum(d1.get(f, 0) * v for f, v in d2.items())

def increment(d1, scale, d2):
    """
    Implements d1 += scale * d2 for sparse vectors.
    @param dict d1: the feature vector which is mutated.
    @param float scale
    @param dict d2: a feature vector.
    """
    for f, v in d2.items():
        d1[f] = d1.get(f, 0) + v * scale

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collection.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    return sum(v1[e]*v2[e] for e in min(v1, v2, key=len).iterkeys())
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for k in v2.iterkeys():
        v1[k] += scale * v2[k]
    # END_YOUR_CODE

def readExamples(path):
    '''
    Reads a set of training examples.
    '''
    examples = []
    for line in open(path):
        # Format of each line: <output label (+1 or -1)> <input sentence>
        y, x = line.split(' ', 1)
        examples.append((x.strip(), int(y)))
    print 'Read %d examples from %s' % (len(examples), path)
    return examples

def evaluatePredictor(examples, predictor):
    '''
    predictor: a function that takes an x and returns a predicted y.
    Given a list of examples (x, y), makes predictions based on |predict| and returns the fraction
    of misclassiied examples.
    '''
    error = 0
    for x, y in examples:
        if predictor(x) != y:
            error += 1
    return 1.0 * error / len(examples)

def outputWeights(weights, path):
    print "%d weights" % len(weights)
    out = open(path, 'w')
    for f, v in sorted(weights.items(), key=lambda (f, v) : -v):
        print >>out, '\t'.join([f, str(v)])
    out.close()

def verbosePredict(phi, y, weights, out):
    yy = 1 if dotProduct(phi, weights) > 0 else -1
    if y:
        print >>out, 'Truth: %s, Prediction: %s [%s]' % (y, yy, 'CORRECT' if y == yy else 'WRONG')
    else:
        print >>out, 'Prediction:', yy
    for f, v in sorted(phi.items(), key=lambda (f, v) : -v * weights.get(f, 0)):
        w = weights.get(f, 0)
        print >>out, "%-30s%s * %s = %s" % (f, v, w, v * w)
    return yy

def outputErrorAnalysis(examples, featureExtractor, weights, path):
    out = open('error-analysis', 'w')
    for x, y in examples:
        print >>out, '===', x
        verbosePredict(featureExtractor(x), y, weights, out)
    out.close()

def interactivePrompt(featureExtractor, weights):
    while True:
        print '> ',
        x = sys.stdin.readline()
        if not x: break
        phi = featureExtractor(x) 
        verbosePredict(phi, None, weights, sys.stdout)

############################################################

def generateClusteringExamples(numExamples, numWordsPerTopic, numFillerWords):
    '''
    Generate artificial examples inspired by sentiment for clustering.
    Each review has a hidden sentiment (positive or negative) and a topic (plot, acting, or music).
    The actual review consists of 2 sentiment words, 4 topic words and 2 filler words, for example:

        good:1 great:1 plot1:2 plot7:1 plot9:1 filler0:1 filler10:1

    numExamples: Number of examples to generate
    numWordsPerTopic: Number of words per topic (e.g., plot0, plot1, ...)
    numFillerWords: Number of words per filler (e.g., filler0, filler1, ...)
    '''
    sentiments = [['bad', 'awful', 'worst', 'terrible'], ['good', 'great', 'fantastic', 'excellent']]
    topics = ['plot', 'acting', 'music']
    def generateExample():
        x = Counter()
        # Choose 2 sentiment words according to some sentiment
        sentimentWords = random.choice(sentiments)
        x[random.choice(sentimentWords)] += 1
        x[random.choice(sentimentWords)] += 1
        # Choose 4 topic words from a fixed topic
        topic = random.choice(topics)
        x[topic + str(random.randint(0, numWordsPerTopic-1))] += 1
        x[topic + str(random.randint(0, numWordsPerTopic-1))] += 1
        x[topic + str(random.randint(0, numWordsPerTopic-1))] += 1
        x[topic + str(random.randint(0, numWordsPerTopic-1))] += 1
        # Choose 2 filler words
        x['filler' + str(random.randint(0, numFillerWords-1))] += 1
        return x

    random.seed(42)
    examples = [generateExample() for _ in range(numExamples)]
    return examples

def outputClusters(path, examples, centers, assignments):
    '''
    Output the clusters to the given path.
    '''
    print 'Outputting clusters to %s' % path
    out = open(path, 'w')
    for j in range(len(centers)):
        print >>out, '====== Cluster %s' % j
        print >>out, '--- Centers:'
        for k, v in sorted(centers[j].items(), key = lambda (k,v) : -v):
            if v != 0:
                print >>out, '%s\t%s' % (k, v)
        print >>out, '--- Assigned points:'
        for i, z in enumerate(assignments):
            if z == j:
                print >>out, ' '.join(examples[i].keys())
    out.close()
