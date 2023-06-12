# -*- coding: utf-8 -*-
"""
Experiment 3
Question 2
Part B

"""

def sum_divide(A, a=0, b=None):
    """  
    Divides list in 2 parts and sends to sum_
    """
    if b is None:
        b = len(A)
    if len(A) == 1:
        return A[0]
    if len(A) == 0:
        return 0
    if 1 < b-a :
        c = (a+b)//2
        L,R = A[a:c],A[c:b]
        return sum_divide(L) + sum_divide(R)

A = [1,3,2,4,10,1,3,2,4,11,19,10]
a = sum_divide(A)
print(f"The sum of {A} is {a}")