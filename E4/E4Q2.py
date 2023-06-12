# -*- coding: utf-8 -*-
"""
Experiment 4
Question 2

"""

def insertionSort(A):
    for i in range(1,len(A),1):
        key = A[i]
        j = binary_search(A[0:i], key)
        for k in range(i,j,-1):
            A[k] = A[k-1]
        A[j] = key
        

def binary_search(A,x):
    if x < A[0]:
        return 0
    else:
        low = 0
        high = len(A)
        mid = (high + low)//2 

        while A[mid] != x and (low+1) != high: 
            if  A[mid] < x:
                low = mid 
            elif A[mid] > x:
                high = mid
            mid = (high + low)//2

        if A[mid] <= x:
            return mid+1
        else:
            return mid-1
            
A = [114,1111,18,10,24,32,45,150]
insertionSort(A)
print(A)