# takes dictionary, builds word tree
import pygtrie
import os
import stat
import sys

lexTree = pygtrie.CharTrie()

f = file('scrabblewords.txt','r')
for w in f:
    lexTree[str.strip(w)] = True



'''

try:
    import termios
    import tty

    def getch():
        """Reads single character from standard input."""
        attr = termios.tcgetattr(0)
        try:
            tty.setraw(0)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(0, termios.TCSADRAIN, attr)

except ImportError:
    try:
        from msvcrt import getch  # pylint: disable=import-error
    except ImportError:
        sys.exit(0)


print 'Start typing a word, "exit" to stop'

print

text = ''
while True:
    ch = getch()
    if ord(ch) < 32:
        print 'Exiting'
        break

    text += ch
    value = lexTree.get(text)
    if value is False:
        print 'Exiting'
        break
    if value is not None:
        print repr(text), 'is a word'
    if lexTree.has_subtrie(text):
        print repr(text), 'is a prefix of a word'
    else:
        print repr(text), 'is not a prefix, going back to empty string'
        text = ''
'''