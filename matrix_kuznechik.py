# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:42:47 2020

@author: IVANKIN
"""

def matrix_kuznechik(N,M):
    A = [[0]*(M+1) for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i==1 and j==1:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j] + A[i][j-1]
            
    return A[N][M]