# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:25:25 2020

@author: IVANKIN
"""

def kuznechik_allowed(N, allowed):
    A = [0,1] + (N-1)*[0]
    
    for i in range(2,N+1):
        if allowed[i]:
            A[i] = A[i-2] + A[i-1]   
     
    return A[N]


