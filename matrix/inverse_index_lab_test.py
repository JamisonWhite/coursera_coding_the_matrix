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


def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    return set.union(*[inverseIndex[w] for w in query])


## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    return set.intersection(*[inverseIndex[w] for w in query])

with open('stories_small.txt') as f:
    D = f.readlines()

ii = makeInverseIndex(D)
print('makeInverseIndex\n', ii)

ir = orSearch(ii, ['need', 'needed'])
print('orSearch\n', ir)

ir = andSearch(ii, ['need', 'needed'])
print('andSearch\n', ir)

ir = orSearch(ii, ['localizes', 'dog'])
print('orSearch\n', ir)

