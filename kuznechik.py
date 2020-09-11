# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:20:21 2020

@author: IVANKIN
"""

def kuznechik(N):
    A = [0,1] + N*[0]
    
    for i in range(2,N+1):
     A[i] = A[i-2] + A[i-1]   
     
    return A[N]