

__author__ = 'jamie'

from vec import Vec
from mat import Mat
from matutil import *
from vecutil import *

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

# Transpose matrix
# my implmentation; forgot about items
# def transpose0(M): return Mat((M.D[1], M.D[0]), {(j, i):M.f[i, j] for j in M.D[1] for i in M.D[0]})
def transpose(M): return Mat((M.D[1], M.D[0]), {(j, i):v for (i, j), v in M.f.items()})

if False:
    print("\nTranspose")
    t = transpose(m)
    print(t)




#teting matrix class
if False:
    M = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
    x = M[1,'a']
    print('expected x=4; actual x=', x)
    y =  M[3,'a']
    print('expected y=0; actual y=', y)
    print(M)


################################
#hw3 p11 M * v
def lin_comb_mat_vec_mult(M, v):
    assert(M.D[1] == v.D)
    from matutil import mat2coldict
    m = mat2coldict(M)
    y = sum([v[d] * m[d] for d in v.D])
    return y

if False:
    M = listlist2mat([[-1, 1, 2], [1, 2, 3], [2, 2, 1]])
    v = list2vec([1, 2, 0])
    print(v)
    print(M)
    print('lin_comb_mat_vec_mult(M) = ', lin_comb_mat_vec_mult(M, v))



################################
# hw3 p12 v * M
def lin_comb_vec_mat_mult(v, M):
    assert(v.D == M.D[0])
    from matutil import mat2coldict
    m = mat2coldict(M)
    y = {d:v * m[d] for d in m.keys()}
    return Vec(m.keys(), y)

v = list2vec([4, 3, 2, 1])
M = listlist2mat([[-5, 10], [-4, 8], [-3, 6], [-2, 4]])
print(v)
print(M)
print('lin_comb_vec_mat_mult(M) = ', lin_comb_vec_mat_mult(v, M))

d1 = {0, 1, 2, 3, 4}
d2 = {'a','b','c','d'}
D1 = (d1, d2)
M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31})
M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})
M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})
M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})
U1 = Vec(d1, {0: 1, 1: 0, 2: 1, 3: 2, 4: 0})
U2 = Vec(d1, {0: 2, 2: 2, 4: 2})
U3 = Vec(d1, {0: 1, 1: 3, 3: 2})



print('lin_comb_vec_mat_mult(M) = ', lin_comb_vec_mat_mult(U1, M1))
print('lin_comb_vec_mat_mult(M) = ', lin_comb_vec_mat_mult(U2, M2))
print('lin_comb_vec_mat_mult(M) = ', lin_comb_vec_mat_mult(U3, M3))



# ################
# print('mat2rowdict(A) = ', mat2rowdict(M))
# print('mat2coldict(A) = ', mat2coldict(M))
# print('mat2rowdict(A) = ', mat2rowdict(M))
# print('mat2coldict(A) = ', mat2coldict(M))
#
