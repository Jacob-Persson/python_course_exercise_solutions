# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:13:53 2026

@author: jacpe396
"""

import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
a = np.zeros(10)
a[4] = 1

#b. Create a vector with values ranging from 10 to 49
b = np.arange(10, 50)

# c. Reverse a vector (first element becomes last)
c = b[::-1]

# d. Create a 3x3 matrix with values ranging from 0 to 8
d = np.arange(9).reshape(3,3)

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
e = np.nonzero([1,2,0,0,4,0])

# f. Create a random vector of size 30 and find the mean value
f_vector = np.random.rand(30)
f_mean = np.mean(f_vector)

# g. Create a 2d array with 1 on the border and 0 inside
g = np.ones([3,3])
g[1,1] = 0

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
h = np.ones((8, 8), dtype=int)

# Fill rows starting at 1, 3, 5, 7 and columns starting at 0, 2, 4, 6
h[1::2, ::2] = 0

# Fill rows starting at 0, 2, 4, 6 and columns starting at 1, 3, 5, 7
h[::2, 1::2] = 0

# i. Create a checkerboard 8x8 matrix using the tile function
i = np.tile([[1, 0], [0, 1]], (4, 4))

#Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[(Z>3) & (Z<8)] = -Z[(Z>3) & (Z<8)]
print(Z)

#k. Create a random vector of size 10 and sort it
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

#l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print(equal)

#m. How to calculate the square of every number in an array in place (without creating temporaries)?
Z = np.arange(10, dtype=np.int32)
print(Z)
Z = Z*Z
print(Z)

#n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(D)