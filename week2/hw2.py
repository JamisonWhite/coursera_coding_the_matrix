# version code 753+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one



## Problem 1
def vec_select(veclist, k): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [v for v in veclist if v[k] == 0]

# print('Calling vec_select')
# D = {'a','b','c'}
# v1 = Vec(D, {'a': 1})
# v2 = Vec(D, {'a': 0, 'b': 1})
# v3 = Vec(D, {        'b': 2})
# v4 = Vec(D, {'a': 10, 'b': 10})
#
# x = vec_select([v1, v2, v3, v4], 'a')
# y = [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
# z = x == y
# print(x)
# print(y)
# print(z)

def vec_sum(veclist, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    return sum(veclist) if any(veclist) else Vec(D, {})

# print('Calling vec_sum')
# D = {'a','b','c'}
# v1 = Vec(D, {'a': 1})
# v2 = Vec(D, {'a': 0, 'b': 1})
# v3 = Vec(D, {        'b': 2})
# v4 = Vec(D, {'a': 10, 'b': 10})
# x = vec_sum([v1, v2, v3, v4], D)
# y = Vec(D, {'b': 13, 'a': 11})
# print(x)
# print(y)
# z = x == y
# print(z)
# print(vec_sum([], D))
# print('Finished vec_sum')

def vec_select_sum(veclist, k, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return vec_sum( vec_select(veclist, k), D )


## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    return [(1/k) * v for k, v in vecdict.items()]

# v1 = Vec({1,2,3}, {2: 9})
# v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
# vecdict = {3: v1, 5: v2}
# result = [(1/k) * v for k, v in vecdict.items()  ]
# print(result)
# #scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]


## Problem 3
def GF2_span(D, L):
    '''
    Constructing the Span of Given Vectors OverGF(2)
    Problem 3:Write a procedureGF2_spanwith the following spec:
     input: a set D of labels and a list L of vectors ove rGF(2) with label-set D
     output:the list of all linear combinations of the vectors in L
    (Hint: use a loop (or recursion) and a comprehension. Be sure to test your procedure on examples where L
    is an empty list.)
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
    vectors = []
    for l in L:
        v = Vec(D, {}) * one
        vectors.append(v)

    return vectors
# for a in (0,1):
#     for b in (0,1):
#         for c in (0,1):
#             y = [a, b, c]




D = {'a', 'b', 'c'}
L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]

print('z...')
z = [[a, b, c] for a in (0,1) for b in (0,1) for c in (0,1)]
print(z)

print('testing...')
x = (0,1)
y = 3
z = [[a, b, c] for a in x for b in x for c in x ]
print(z)

print('Starting Problem 3\n D = ', D, '\n L = ', L)
a = len(GF2_span(D, L))
print(a) #4


b = Vec(D, {}) in GF2_span(D, L)
print(b) #True
c = Vec(D, {'b': one}) in GF2_span(D, L)
print(c) #True
d = Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
print(d) #True
e = Vec(D, {x:one for x in D}) in GF2_span(D, L)
print(e) #True

## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = ...
is_it_a_vector_space_2 = ...



## Problem 5
is_it_a_vector_space_3 = ...
is_it_a_vector_space_4 = ...


## Problem 6

is_it_a_vector_space_5 = ...
is_it_a_vector_space_6 = ...
