#!/usr/bin/env checkio --domain=py run matrix-transpose

# In linear algebra, the transpose of a matrixAis another matrixAT(also writtenA′,Atr,tAorAt) created by any one of the following equivalent    actions:
# 
# reflectAover its main diagonal (which runs from top-left to        bottom-right) to obtainATwrite the rows ofAas the columns ofATwrite the columns ofAas the rows ofATFormally, theithrow,jthcolumn element ofATis thejthrow,ithcolumn element ofA:
# 
# [AT]i j= [A]j i
# 
# IfAis anm×nmatrix thenATis ann×mmatrix.
# 
# You have been given a matrix as a 2D list with integers.    Your task is to return a transposed matrix based on input.
# 
# Input:A matrix as a list of lists with integers.
# 
# Output:The transposed matrix as a list/tuple of lists/tuples with integers.
# 
# Precondition:
# 0 < len(matrix) < 10
# all(0 < len(row) < 10 for row inmatrix)
# 
# 
# END_DESC

from typing import List
from numpy import array, transpose

''' With numpy '''
def checkio(matrix: List[List[int]]) -> List[List[int]]:
    matrix = array(matrix,int).transpose()
    rows = matrix.shape[0]
    return [list(matrix[i,:]) for i in range(rows)]

''' Without numpy '''
def checkio(matrix: List[List[int]]) -> List[List[int]]:
    cols = len(matrix[0])
    matrix2 = []
    for i in range(cols):
        col = []
        for row in matrix:
            col.append(row[i])
        matrix2.append(col)
    return matrix2