# -*- coding: utf-8 -*-
"""
Experiment 6
Question 1

Counting Sort assumes +ve keys
Radix

"""
class Att():
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.digits = [] # Digits stored is reverse
    def __str__(self):
        return str(self.key)


def Counting_Sort(A,k=None):
    "Sort A assuming items have non-negative keys"
    if k == None:
        u = 1 + max([x.key for x in A])        # O(n) find maximum key
        D = [[] for i in range(u)]                  # O(u) direct access array of chains
        for x in A:                                 # O(n) insert into chain at x.key
            D[x.key].append(x)
    else:
        u = 1 + max([x.digits[k] for x in A])  # O(n) find maximum key
        D = [[] for i in range(u)]                  # O(u) direct access array of chains
        for x in A:                                 # O(n) insert into chain at x.key
            D[x.digits[k]].append(x)
        
    i = 0
    for j in D:
        for x in j:                                 # O(u) read out items in order
            A[i] = x
            i += 1  
            
def Radix_Sort(A):
    keys = [ abs(x.key) for x in A]                 
    n = len(A)
    u = 1 + max(keys)
    dgt = (u.bit_length() // n.bit_length())
    for j in range(dgt):
        for i in range(len(A)): # Save last digit first
            a =  ( abs(A[i].key) // (10**j)) % 10    
            A[i].digits.append(a)
        Counting_Sort(A,j)

def Radix(A):
    keys = [x.key for x in A]           # O(1)
    if min(keys) < 0:                   # O(1)
        B = []                          # O(1)
        C = []                          # O(1)
        for i in A:                     # O(n)
            if i.key < 0:               # O(1)
                B.append(i)             # O(1)
            else:                       # O(1)
                C.append(i)             # O(1)
        if B != [] :                    # O(1)
            Radix_Sort(B)               # O(n+b)
        if C != [] :                    # O(1)
            Radix_Sort(C)               # O(n+b)
        b = []                          # O(1)
        for i in range(len(B)):         # O(n)
            b.append(B[len(B)-1 - i])   # O(1)
        D = b + C                       # O(1)
        for i in range(len(D)):         # O(n)
            A[i] = D[i]                 # O(1)
    else:                               # O(1)
        Radix_Sort(A)                   # O(n+b)
        
def gen_list():
    A = []
    x = [123,-19,-723,-123,479]
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
Radix(A)
print_(A)