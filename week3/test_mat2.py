__author__ = 'Jamie'

from mat import Mat
from vec import Vec
from GF2 import one

# No operations should mutate the input matrices, except setitem.

print('For getitem(M,k):')

M = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
print(M[1,'a'] == 4)
print(M[3,'a'] == 0)
print(M == M)
# Make sure your operations work on other fields, like GF(2).

M = Mat((set(range(1000)), {'e',' '}), {(500, ' '): one, (255, 'e'): 0})
print(M[500, ' '] == one)
print(M[500, 'e'] == 0)
print(M[255, 'e'] == 0)
print(Mat((set(range(1000)), {'e',' '}), {(500, ' '): one, (255, 'e'): 0}) == M)
# True


print('For setitem(M,k,val)')
    
M = Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):7})
M['b', 5] = 9
M['c', 5] = 13
print(M == Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):9, ('c',5):13}))
# True

print('Make sure your operations work with bizarre and unordered keys.')

N = Mat(({((),), 7}, {True, False}), {})
N[(7, False)] = 1
N[(((),), True)] = 2
print(N == Mat(({((),), 7}, {True, False}), {(7,False):1, (((),), True):2}))
# True

print('For add(A, B):')

A1 = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})
A2 = Mat(({3, 6}, {'x','y'}), {(3,'y'):4})
B = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (3,'y'):4, (6,'y'):3})
print(A1 + A2 == B)
# True
print(A2 + A1 == B)
# True
print(A1 == Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3}))
# True
zero = Mat(({3,6}, {'x','y'}), {})
print(B + zero == B)
# True
C1 = Mat(({1,3}, {2,4}), {(1,2):2, (3,4):3})
C2 = Mat(({1,3}, {2,4}), {(1,4):1, (1,2):4})
D = Mat(({1,3}, {2,4}), {(1,2):6, (1,4):1, (3,4):3})
print(C1 + C2 == D)
# True



print('For scalar_mul(M, x):')

M = Mat(({1,3,5}, {2,4}), {(1,2):4, (5,4):2, (3,4):3})
print(0*M == Mat(({1, 3, 5}, {2, 4}), {}))
# True
print(1*M == M)
# True
print(0.25*M == Mat(({1,3,5}, {2,4}), {(1,2):1.0, (5,4):0.5, (3,4):0.75}))
# True

M = Mat(({1,2,3},{4,5,6}), {(1,4):one, (3,5):one, (2,5): 0})
print(one * M == Mat(({1,2,3},{4,5,6}), {(1,4):one, (3,5):one, (2,5): 0}))
# True
print(0 * M == Mat(({1,2,3},{4,5,6}), {}))
# True

    
print('For equal(A, B):')

print(Mat(({'a','b'}, {0,1}), {('a',1):0}) == Mat(({'a','b'}, {0,1}), {('b',1):0}))
# True
A = Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1})
B = Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1, ('b',1):0})
C = Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1, ('b',1):5}) 
print(A == B)
# True
print(A == C, " (False expected)")
# False
print(A == Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1}))
# True


print('For transpose(M):')

M = Mat(({0,1}, {0,1}), {(0,1):3, (1,0):2, (1,1):4})
print(M.transpose() == Mat(({0,1}, {0,1}), {(0,1):2, (1,0):3, (1,1):4}))
# True
M = Mat(({'x','y','z'}, {2,4}), {('x',4):3, ('x',2):2, ('y',4):4, ('z',4):5})
Mt = Mat(({2,4}, {'x','y','z'}), {(4,'x'):3, (2,'x'):2, (4,'y'):4, (4,'z'):5})
print(M.transpose() == Mt)
# True


print('For vector_matrix_mul(v, M):')

v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
M1 = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7})
print(v1*M1 == Vec({1, 2, 3},{1: -8, 2: 2, 3: 0}))
# True
print(v1 == Vec({1, 2, 3}, {1: 1, 2: 8}))
# True
print(M1 == Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7}))
# True
v2 = Vec({'a','b'}, {})
M2 = Mat(({'a','b'}, {0, 2, 4, 6, 7}), {})
print(v2*M2 == Vec({0, 2, 4, 6, 7},{}))
# True


print('For matrix_vector_mul(M, v):')

N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
print(N1*u1 == Vec({1, 3, 5, 7},{1: 3, 3: 9, 5: -2, 7: 3}))
# True
print(N1 == Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1}))
# True
print(u1 == Vec({'a', 'b'}, {'a': 1, 'b': 2}))
# True
N2 = Mat(({('a', 'b'), ('c', 'd')}, {1, 2, 3, 5, 8}), {})
u2 = Vec({1, 2, 3, 5, 8}, {})
print(N2*u2 == Vec({('a', 'b'), ('c', 'd')},{}))
# True

print('For matrix_matrix_mul(A, B):')

A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(A*B == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31}))
# True
C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2}) 
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(C*D == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5}))
# True
M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
print(M*N == Mat(({0,1}, {(1,1), (2,2)}), {}))
# True


print('finished')
exit()
