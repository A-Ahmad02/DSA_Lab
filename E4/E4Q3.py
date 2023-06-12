# -*- coding: utf-8 -*-
"""
Experiment 4
Question 3

"""

# def selectionSort(A):
#     n = len(A) # 1
#     for i in range(0,n-1,1): # n
#         y = x = A[i] # n-1 (x and y)
#         k = i # n-1
#         for j in range(i,n,1): # (t=2 to n)sum(t) +1
#             if A[j] <= y: # (t=2 to n)sum(t)
#                 y = A[j] # Worst case -> (t=2 to n)sum(t)
#                 k = j # Worst case -> (t=2 to n)sum(t)

#         A[i] = y  # n-1
#         A[k] = x  # n-1
#     print(A) # 1
    
# A = [41,2,2,3,1,9,10,29,3,500] # 1
# selectionSort(A) 

def selectionSort(A):
    for i in range(len(A)-1): # n
        key = A[i] # n-1
        index = i # n-1
        j = i + 1 # n-1
        while j < len(A): # 0.5n^2 - 0.5n
            if A[j] < key:
                key = A[j]
                index = j
            j += 1
        A[index] = A[i]
        A[i] = key

A = [41,2,2,3,1,9,10,29,3,500,0] # 1
selectionSort(A)  
print(A)      
                