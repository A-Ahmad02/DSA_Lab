# -*- coding: utf-8 -*-
"""
Experiment 1
Question 4

Linear Search

"""

def linear_search(A,v):
    for i in range(0,len(A),1):
        if A[i] == v:
            return str(v)+" exists in the list at index "+str(i)
    return "NIL"

A = [5,2,3,4,400]
v = int(input("Enter a number:\t"))
print(linear_search(A,v))

