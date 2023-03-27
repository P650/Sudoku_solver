# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:27:55 2022

@author: Pavankumar
"""



# matrix =      [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#                [6, 0, 0, 1, 9, 5, 0, 0, 0],
#                [0, 9, 8, 0, 0, 0, 0, 6, 0],
#                [8, 0, 0, 0, 6, 0, 0, 0, 3],
#                [4, 0, 0, 8, 0, 3, 0, 0, 1],
#                [7, 0, 0, 0, 2, 0, 0, 0, 6],
#                [0, 6, 0, 0, 0, 0, 2, 8, 0],
#                [0, 0, 0, 4, 1, 9, 0, 0, 5],
#                [0, 0, 0, 0, 8, 0, 0, 7, 9]]


matrix =      [[8, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 3, 6, 0, 0, 0, 0],
               [0, 7, 0, 0, 9, 0, 2, 0, 0],
               [0, 5, 0, 0, 0, 7, 0, 0, 0],
               [0, 0, 0, 0, 4, 5, 7, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 3, 0],
               [0, 0, 1, 0, 0, 0, 0, 6, 8],
               [0, 8, 5, 0, 0, 0, 0, 1, 0],
               [0, 9, 0, 0, 0, 0, 4, 0, 0]]

def isValid(matrix, x, y, val):
    
    for j in range(0, 9):
        if (matrix[x][j] == val):
            return False
        
    for i in range(0, 9):
        if (matrix[i][y] == val):
            return False
        
    submati = x-(x%3)
    submatj = y-(y%3)
    
    for i in range(0, 3):
        for j in range(0, 3):
            if(matrix[submati + i][submatj + j] == val):
                return False
            
    return True


def sudokoSolver(matrix, i, j):
    
    if j == 9:
        
        if i == 8:
            
            return True
        
        i += 1
        j = 0
        
    if matrix[i][j] > 0:
        
        return sudokoSolver(matrix, i, j+1)
    
    for val in range(1, 10):
        
        if (isValid(matrix, i, j, val)):
            
            matrix [i][j] = val
            
            if sudokoSolver(matrix, i, j+1):
                
                return True
            
            
        matrix[i][j] = 0
        
    return False


print(sudokoSolver(matrix, 0, 0))

print(matrix)
