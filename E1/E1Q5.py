# -*- coding: utf-8 -*-
"""
Experiment 1
Question 5

"""

def min_mod_tuple(A,k):
    n = len(A)
    i_j = [(0,1)]
    min_mod = (A[0]*A[1])%k
    
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            mod = (A[i]*A[j])%k
            if mod < min_mod:
                min_mod = mod
                i_j = [(i,j)]
            elif mod == min_mod and (i,j) != (0,1):
                i_j.append((i,j))
                
    return i_j

A = [5,2,3,4]
k = int(input("Enter a number:\t"))
z= min_mod_tuple(A,k)
print(z)