# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 08:47:02 2020

@author: IVANKIN
"""

def merge(A,B):
    
    i = 0
    j = 0

    out = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1

    return out
    
def merge_sort(A):
    if len(A) <= 1:
        return A
    
    middle = len(A)//2
    left = []
    right = []
    
    for i in range(middle):
        left.append(A[i])
    for i in range(middle,len(A)):
        right.append(A[i])
        
    left = merge_sort(left)
    right = merge_sort(right)
    
    C = []
    C = merge(left, right)

    
    return C

in_array = [5,4,3,2,1,19,-8,1,3,3,3,3,2,6,-3,0,0,0]
out = merge_sort(in_array)
print(out)