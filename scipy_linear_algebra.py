# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:44:25 2026

@author: jacpe396
"""

import numpy as np
from scipy import linalg

# a. Define matrix A
A = np.array([[1, -2, 3],
              [4, 5, 6],
              [7, 1, 9]])

# b. Define vector b
b = np.array([1, 2, 3])

# c. Solve the linear system of equations A x = b
x = linalg.solve(A, b)

print("Solution vector x:")
print(x)

# Verification: A @ x should equal b
print("\nVerification (A @ x):")
print(A @ x)

# Repeat using a random 3x3 matrix B
B = np.random.rand(3,3)
x = linalg.solve(A,B)
print("Solution vector x:")
print(x)

# Verification: A @ x should equal B
print("\nVerification (A @ x):")
print(A @ x)

# Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors (as columns):")
print(eigenvectors)

# Calculate the inverse, determinant of A
# Calculate Determinant
det_A = np.linalg.det(A)

# Calculate Inverse
inv_A = np.linalg.inv(A)

print(f"Determinant: {det_A:.2f}")
print("Inverse Matrix:")
print(inv_A)

# Calculate the norm of A with different orders
# 1. Frobenius Norm (Default)
frob_norm = np.linalg.norm(A) 

# 2. L2 Norm (Spectral Norm)
l2_norm = np.linalg.norm(A, ord=2)

# 3. L1 Norm (Maximum Column Sum)
l1_norm = np.linalg.norm(A, ord=1)

# 4. Infinity Norm (Maximum Row Sum)
inf_norm = np.linalg.norm(A, ord=np.inf)