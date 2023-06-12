# -*- coding: utf-8 -*-
"""
Experiment 1
Question 1

Insertion Sort
Ascending Order

"""

def insertion_sort(A):
    for j in range(1,len(A),1):
        key = A[j]
        i = j - 1
#         Insertion Code
        while (i>=0) and (A[i]>key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


A = [5,2,4,6,1,3]
print(insertion_sort(A))