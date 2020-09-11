# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:16:40 2020

@author: IVANKIN
"""
import random

def quicksort(A):
    if len(A) == 0:
        return
    
    barrier = random.choice(A)
    left = []
    middle = []
    right = []
    
    for x in A:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
            
    quicksort(left)
    quicksort(right)
    
    k = 0
    for x in left+middle+right:
        A[k] = x
        k += 1


in_array = [0,5,4,3,2,1,19,-8,1,3,3,3,3,2,6,-3,0,0,0]
quicksort(in_array)
print(in_array)