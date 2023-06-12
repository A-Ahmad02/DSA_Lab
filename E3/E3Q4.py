# -*- coding: utf-8 -*-
"""
Experiment 3
Question 4

"""

def insertionSort(A,j=None):
    
    if j == 1:
        return 
    elif j == None:
        j = len(A)-1
    
    insertionSort(A,j-1)
    
    key = A[j]
    i = j - 1
    while (i > -1 and A[i] > key):
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
    
# def insertionSort(A,j=1):
#     if j == len(A):
#         return
    
#     key = A[j]
#     i = j - 1
#     while (i > -1 and A[i] > key):
#         A[i+1] = A[i]
#         i = i - 1
#     A[i+1] = key
#     insertionSort(A,j+1)

A = [1,5,4,2,3,7,0,10,21,15,12,1,0]
insertionSort(A)
print(A)

