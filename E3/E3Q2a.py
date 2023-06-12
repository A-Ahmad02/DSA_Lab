# -*- coding: utf-8 -*-
"""
Experiment 3
Question 2
Part A

"""

def sum_(A):
    if len(A) == 1:
        return A[0]
    return sum_(A[1:]) + A[0]


A = [1,3,2,4,11,19,10]
a = sum_(A)
print(f"The sum of {A} is {a}")