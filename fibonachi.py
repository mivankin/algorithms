# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:57:10 2020

@author: IVANKIN
"""

def fibonachi(N):
    F = [1,1] + N*[0]
    for i in range(2,N):
        F[i] = F[i-2] + F[i-1]
        
    return F[N-1]
        