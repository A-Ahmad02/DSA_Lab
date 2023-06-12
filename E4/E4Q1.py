# -*- coding: utf-8 -*-
"""
Experiment 4
Question 1

"""
# def binary_search(A,x):
#     low = 0
#     high = len(A)
#     mid = (high + low)//2 

#     while A[mid] != x and (low+1) != high: 
#         if  A[mid] < x:
#             low = mid 
#         elif A[mid] > x:
#             high = mid
#         mid = (high + low)//2

#     if A[mid] == x:
#         print(f"{x} exists in the list at index {mid}")
#     else:
#         print("NIL")

def Search(A, x, low=0, high= None):
    
    if high == None:
        high = len(A)
    
    mid = (high + low) // 2
    
    if A[mid] == x:
        print(f"{x} exists in the list at index {mid}")
        return 
    elif (low+1) == high:
        print("NIL")
        return

    if  A[mid] < x:
        low = mid 
    elif A[mid] > x:
        high = mid
    
    return Search(A, x, low, high)
    
    

    

A = [1,2,3,4,20,55,90,111]
# binary_search(A,20)
Search(A,20)