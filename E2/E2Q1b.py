# -*- coding: utf-8 -*-
"""
Experiment 2
Question 1
Part B

"""
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(A):
    """  
    Sorts the given list in Ascending Order
    """
    for j in range(1,len(A),1):
        key = A[j]
        i = j - 1
#         Insertion Code
        while (i>=0) and (A[i]>key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
     

def foo(case,start,stop,gap):
    n = [i for i in range(start,stop,gap)] 
    A = range(0,10000,1)
    y = [] 
    for j in n: # Set length of array
        """
        Calculates Average time to sort a j element array
        """
        runT = []
        trials = 10
        for i in range(0,trials,1):
            B = [random.choice(A) for _ in range(j)] 
            if case == 'worstcase':
                B.sort(reverse=True)  # Descending Order   
            elif case == 'bestcase':
                B.sort() # Ascending Order
            t1 = time.time()
            insertion_sort(B)
            t2 = time.time()
            td = (t2 - t1)* 1000
            runT.append(td)
            print(f"n = {j}  trialno = {i+1}  runTime = {td}ms")
        avgT = sum(runT) /trials
        y.append(avgT) # List of average time taken
        print(f"avg {case} runTime over {trials} trails for n = {j} is {avgT}ms")
        
            
    """  
    Plots Fitted Curve of n against average run time taken to sort
    """
    n = np.array(n)
    y = np.array(y)
    if case == 'worstcase': # Time complexity O(n**2)
        eq = np.polyfit(n,y,2) # Outputs quadratic coefficients
        p = (eq[0]*(n**2)) +  (eq[1]*n) + eq[2] # Forming quadratic function
        c = "red"
        name = "Worst Case"
    elif case == 'bestcase': # Time complexity O(n)
        eq = np.polyfit(n,y,1) # Outputs linear coefficients
        p = (eq[0]*n) + eq[1]  # Forming linear function
        c = "blue"
        name = "Best Case"
    plt.figure(figsize=(9,6))
    plt.rc('font', size=20)  
    plt.plot(n,p,color=c) # Plots
    plt.xlabel('Amount of numbers (n)')
    plt.ylabel('Runtime (ms)')
    plt.title('Runtime VS n plot')
    plt.legend([name])
    plt.grid()
    
    
    """
    Calculate coefficient of determination R**2
    """
    u = sum(y)/len(y)
    R = 1 - (sum((y-p)**2)/sum((y-u)**2))
    print(f"R**2 = {R}")
    
    
foo('worstcase',0,2000,100)
foo('bestcase',0,20000,1000)
