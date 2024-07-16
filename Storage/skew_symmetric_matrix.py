#!/usr/bin/env checkio --domain=py run skew-symmetric-matrix

# In mathematics, particularly in linear algebra,    a skew-symmetric matrix (also known as an antisymmetric or antimetric) is a square matrixAwhich is transposed    and negative.    This means that it satisfies the equationA = −AT.If the entry in the i-th row and j-th column is aij, i.e.A = (aij)then the symmetric condition becomesaij= −aji.
# 
# You should determine whether the specified square matrix is skew-symmetric    or not.
# 
# You can find more details on Skew-symmetric matrices on itsWikipedia page.
# 
# Input:A square matrix as a list of lists with integers.
# 
# Output:If the matrix is skew-symmetric or not as a boolean.
# 
# Precondition:0 < N < 5
# 
# 
# 
# END_DESC

from numpy import array

def checkio(A):
    M = - array(A).transpose() # M = −A^T
    C = A == M # checks which elements of matrix A are equal to the elements of matrix M in the same positions
    return C.all() # if all of elements are equal return True