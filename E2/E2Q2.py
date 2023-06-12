# -*- coding: utf-8 -*-
"""
Experiment 2
Question 2

"""

def sort(A):
    n = len(A) # 1
    for i in range(0,n-1,1): # n
        y = x = A[i] # n-1
        k = i # n-1
        for j in range(i,n,1): # (t=2 to n)sum(t) +1
            if A[j] <= y: # (t=2 to n)sum(t)
                y = A[j] # Worst case -> (t=2 to n)sum(t)
                k = j # Worst case -> (t=2 to n)sum(t)

        A[i] = y  # n-1
        A[k] = x  # n-1
    print(A) # 1
    
A = [41,2,2,3,1,9,10,29,3,500] # 1
sort(A) 
 