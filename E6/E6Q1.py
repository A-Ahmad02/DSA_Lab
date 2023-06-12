# -*- coding: utf-8 -*-
"""
Experiment 6
Question 1

"""

class Att():
    def __init__(self,key,data):
        self.key = key
        self.data = data
    def __str__(self):
        return str(self.key)



def counting_sort(A):
    "Sort A assuming items have non-negative keys"
    u = 1 + max([x.key for x in A]) # O(n) find maximum key
    D = [[] for i in range(u)]      # O(u) direct access array of chains
    for x in A:                     # O(n) insert into chain at x.key
        D[x.key].append(x)
    i = 0
    
    for chain in D:
        for x in chain: # O(u) read out items in order
            A[i]
            i += 1  
            
def radix_sort(A):
    "Sort A assuming items have non-negative key"
    n = len(A)
    u = 1 + max([x.key for x in A])
    c = 1 + (u.bit_length() // n.bit_length())
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item
    print_(A)
        
        
def gen_list():
    A = []
    x = [123,19,723,123,479]
    for i in x:
        a = Att(i,"data")
        A.append(a)
    return A
    
def print_(A):
    str_ = ""
    for i in A:
        str_ += str(i.key)+" "
    print(str_)

A = gen_list()

print_(A)
radix_sort(A)
print_(A)