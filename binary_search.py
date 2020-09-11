# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:39:12 2020

@author: IVANKIN
"""

def left_binary_search(A, key):
    left_bound = -1
    right_bound = len(A)
    
    while right_bound - left_bound > 1:
        middle = (right_bound + left_bound)//2
        if A[middle] < key:
            left_bound = middle
        else:
            right_bound = middle
            
    return left_bound

def right_binary_search(A, key):
    left_bound = -1
    right_bound = len(A)
    
    while right_bound - left_bound > 1:
        middle = (right_bound + left_bound)//2
        if A[middle] <= key:
            left_bound = middle
        else:
            right_bound = middle
            
    return right_bound
