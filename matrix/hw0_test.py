# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
    return [n for n in L if n % num != 0]


## Problem 2
def myLists(L):
    return [list(range(1, x + 1)) for x in L]


L = [0, 1, 2, 3, 4]
num = 2
print('myFilter\n', myFilter(L, num))

print('myLists\n', myLists(L))


## Problem 3
def myFunctionComposition(f, g):
    return {fk: g[fv] for fk, fv in f.items() if fv in g.keys()}

f = {0:'a', 1:'b'}
g = {'a':'apple', 'b':'banana'}
print('myFunctionComposition\n', myFunctionComposition(f, g))

L = [l + 10 for l in L]
print('L\n', L)

## Problem 6
def mySum(L):
    current = 0
    for x in L:
        current = current + x
    return current

print('mySum\n', mySum(L))

## Problem 7
def myProduct(L):
    current = 1
    for x in L:
        current = current * x
    return current

print('myProduct\n', myProduct(L))


## Problem 8
def myMin(L):
    current = L[0] if len(L) > 0 else 0
    for x in L:
        current = x if x < current else current
    return current

print('myMin\n', myMin(L))


## Problem 9
def myConcat(L):
    current = ''
    for x in L:
        current = current + x
    return current

L2 = ['he', 'she', 'dog']

print('myConcat\n', myConcat(L2))


## Problem 10
def myUnion(L):
    current = set()
    for x in L:
        current = current.union(x)
    return current

L3 = [{0,1}, {0,1,2}, {0,1,2,3,4}]

print('myUnion\n', myUnion(L3))



