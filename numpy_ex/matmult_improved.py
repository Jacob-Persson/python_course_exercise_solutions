# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:09:52 2026

@author: jacpe396
"""

# Program to multiply two matrices using numpy
import numpy as np

N = 250

# NxN matrix
X = np.random.randint(0,100, size=(N,N))

# Nx(N+1) matrix
Y = np.random.randint(0,100, size=(N,N+1))

# result is Nx(N+1)
result = X @ Y

np.set_printoptions(threshold=np.inf)
print(result)
