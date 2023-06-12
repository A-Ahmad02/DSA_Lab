# -*- coding: utf-8 -*-
"""
Experiment 3
Question 1

"""

import random
import time
import numpy as np
import matplotlib.pyplot as plt

code_Stime = time.time()

def merge_sort(A, a=0, b=None):
    """  
    Sorts the given list in Ascending Order
    """
    if b is None:
        b = len(A)
    if 1 < b-a :
        c = (a+b+1)//2
        merge_sort(A,a,c)
        merge_sort(A,c,b)
        L,R = A[a:c],A[c:b]
        merge(L,R,A,len(L),len(R),a,b)
        
def merge(L,R,A,i,j,a,b):
    if a < b :
        if (j==0) or (i>0 and L[i-1]>R[j-1]):
            A[b-1] = L[i-1]
            i = i - 1
        else:
            A[b-1] = R[j-1]
            j = j - 1
        merge(L,R,A,i,j,a,b-1)

     
def foo(start,stop,gap):
    n = [i for i in range(start,stop,gap)] 
    print(n)
    A = range(0,10000,1)
    y = [] 
    xa = []
    ya = []
    for j in n: # Set length of array
        """
        Calculates Average time to sort a j element array
        """
        runT = []
        trials = 10
        for i in range(0,trials,1):
            B = [random.choice(A) for _ in range(j)] 
            B.sort(reverse=True)  # Descending Order 
            t1 = time.time()
            merge_sort(B)
            t2 = time.time()
            td = (t2 - t1)* 1000
            runT.append(td)
            xa.append(j)
            ya.append(td)
            print(f"n = {j}  trialno = {i+1}  runTime = {td}ms")
        avgT = sum(runT) /trials
        y.append(avgT) # List of average time taken
        print(f"avg worstcase runTime over {trials} trails for n = {j} is {avgT}ms")
        
            
    """  
    Plots Fitted Curve of n against average run time taken to sort
    """

    n2 = xa*np.log2(xa)
    eq = np.polyfit(n2,ya,1) # Outputs quadratic coefficients
    p = (eq[0]*n2) + eq[1] # Forming quadratic function
    
    """
    Calculate coefficient of determination R**2
    """
    ya = np.array(ya)
    u = sum(ya)/len(ya)
    R = (1 - (sum((ya-p)**2)/sum((ya-u)**2)))


    plt.figure(figsize=(9,6))
    plt.rc('font', size=20)  
    plt.plot(xa,ya,label="Actual",marker='o',linestyle='') # Plots
    plt.plot(xa,p,label=f"Best Fit with Accuracy {R*100:0.1f}") # Plots
    plt.xlabel('Amount of numbers (n)')
    plt.ylabel('Runtime (ms)')
    plt.title('Runtime VS n plot')
    plt.legend()
    plt.grid()
    
    
foo(100,3000,50)

code_Ftime = time.time()
print("It took ",code_Ftime - code_Stime, "seconds to run")
