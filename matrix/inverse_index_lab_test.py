__author__ = 'jamie'

from dictutil import *

## Task 4
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    #wordlist
    index = {}
    for d in enumerate(strlist):
        words = d[1].split()
        for w in words:
            if w not in index.keys():
                index[w] = set()
            index[w].add(d[0])

    return index

D =['a x', 'b y a', 'c z b']
print(makeInverseIndex(D))

with open('stories_small.txt') as f:
    D = f.readlines()
    print(makeInverseIndex(D))
