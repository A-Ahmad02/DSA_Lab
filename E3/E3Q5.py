# -*- coding: utf-8 -*-
"""
Experiment 3
Question 5

"""

import random

def guess(k,Lb=0,Ub=None): # recursive
    if Ub==None:
        i = random.randint(0,100)
        i = i*100
    else:
        i = (Ub+Lb)//2
    
    if k == i: # Base Case
        print(f"The guess is {i} and the actual number is {k}")
        return i
    elif k > i:
        Lb = i
    else:
        Ub = i

    return guess(k,Lb,Ub)

guess(45)