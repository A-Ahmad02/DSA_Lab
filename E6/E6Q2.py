# -*- coding: utf-8 -*-
"""
Experiment 6
Question 2
Part b

Counting Sort assumes +ve keys

"""
import string

class MelonUsk():
    def __init__(self,key):
        self.key = key
        self.alpha = [ i.lower() for i in (key)]  # Alphabets stored in order
    def __str__(self):
        return str(self.key)


def Counting_Sort(A,k=None):
    "Sort A assuming items have non-negative keys"
    if k == None:
        alphabets = list(string.ascii_lowercase)
        D = [[] for i in range(len(alphabets))]             # O(u) direct access array of chains
        for x in A:                                 # O(n) insert into chain at x.key
            D[ord(x.alpha[k])-97].append(x)
    else:
        alphabets = list(string.ascii_lowercase)
        D = [[] for i in range(len(alphabets))]                  # O(u) direct access array of chains
        for x in A:                       # O(n) insert into chain at x.key
            D[ord(x.alpha[k])-97].append(x)

    i = 0
    for j in D:
        for x in j:                                 # O(u) read out items in order
            A[i] = x
            i += 1  
            
def Martian_Sort(A,order=None):
    keys = [ x.key for x in A] 
    if order == None: 
        dgt = len(keys[0])        
        order = [ k for k in range(dgt)] 
    order.sort(reverse=True)
    for j in order:
        Counting_Sort(A,j)

        
def gen_list():
    A = []
    x = ["bet","bag","rag","rat","bar","bat","bit","beg","biz"]
    for i in x:
        a = MelonUsk(i)
        A.append(a)
    return A
    
def print_(A):
    str_ = ""
    for i in A:
        str_ += str(i.key)+" "
    print(str_)

A = gen_list()
order = [0,2,1]

Martian_Sort(A,order)
print_(A)