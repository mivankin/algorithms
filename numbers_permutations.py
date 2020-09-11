# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:43:16 2020

@author: IVANKIN
"""

def find(number, A):
    for x in A:
        if number == x:
            return True
        return False
    
    
def numbers_permutations(N:int, M:int=-1, prefix=None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return

    for i in range(1, N+1):
        if find(i, prefix):
            continue
        prefix.append(i)
        numbers_permutations(N, M-1, prefix)
        prefix.pop()
        
    