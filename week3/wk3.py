

__author__ = 'jamie'

from vec import Vec
from mat import Mat

'''
Lecture 1 notes
'''

#list of rows
if False:
    print("\n3x4 list of rows; M[i,j] = 0")
    print([[0 for j in range(4)] for i in range(3)])

#list of columns
if False:
    print("\n3x4 list of columns ; M[i,j]=i-j")
    print([[i-j for i in range(3)] for j in range(4)])

#matrix class
#sample from slides
m = Mat(({'a','b'}, {'@', '#', '?'}), {('a','@'):1, ('a','#'):2, ('a','?'):3, ('b','@'):10, ('b','#'):20, ('b','?'):30})

#matrix class
if False:
    print("\nMatrix class")
    m = Mat(({1, 2, 3},{1, 2, 3}), {(1,1):1, (2,2):1})
    print(m)

# Identity creator
def identity(D): return Mat((D, D), {(i, i):1 for i in D})

if False:
    print("\nIdentity Matrix")
    D = {0, 1, 2, 3}
    print(identity(D))

# Matrix to column dictionary
def mat2coldict(A): return {j:Vec(A.D[0], {i:A.f[i, j] for i in A.D[0]}) for j in A.D[1]}

if False:
    print("\nMatrix to column dictionary")
    print(mat2coldict(m))




#teting matrix class
if False:
    M = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
    x = M[1,'a']
    print('expected x=4; actual x=', x)
    y =  M[3,'a']
    print('expected y=0; actual y=', y)
    print(M)



def lin_comb_mat_vec_mult(M, v):
    pass


from matutil import *

A = listlist2mat([[-1, 1, 2], [1, 2, 3], [2,2,1]])
B = listlist2mat([[1], [2], [0]])

print(A)
print(B)

D = A.D
for r in D[0]:
    for c in D[1]:
        print(r, c)






