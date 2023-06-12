# -*- coding: utf-8 -*-
"""
Experiment 5
Question 3

"""

class Node():
    def __init__(self,data,nextNode=None):
        self.data = int(data)
        self.next = nextNode

class LinkedList():
    def __init__(self,A):
        if A == []:
            self.head = None
            self.length = 0
            return
            
        self.head = Node(A[0])
        self.length = len(A)
        
        old = self.head
        for i in range(1,self.length,1):
            new = Node(A[i])
            old.next = new
            old = new
            
        self.tail = old
    
    def insertFirst(self,x):
            
        new = Node(x)
        new.next = self.head
        self.head = new
    
    def deleteFirst(self):
        
        self.head = self.head.next
        self.head.prev = None
        
    def __len__(self):
        return self.length
    
    def __getitem__(self,i):
        if i >= self.length:
            print("Index is not in list")
            return None
        k = self.head
        j = 0
        if j == i:
            return k.data
        while k.next and j <= i:
            k = k.next
            j += 1
            if j == i:
                return k.data
        return "Why??"
        
            
    def __setitem__(self,i,a):
        if i == self.length:
            print("Index NOT in list. \nMaking New Node...")
            self.length += 1
            new = Node(a)
            self.tail.next = new
            self.tail = new
        elif i > self.length:
            print(f"Index NOT in list. \nThe list has {self.length} elements.")
        else:   
            k = self.head
            j = 0
            if j == i:
                k.data = a
            while k.next and j <= i:
                k = k.next
                j += 1
                if j == i:
                    k.data = a
        return "Why??"
                
        
        
    def __str__(self):
        k = self.head
        string = str(k.data)
        while k.next:
            k = k.next
            string += (", "+str(k.data))
        return "["+string+"]"
            
def stores_digits(n):
    A = LinkedList([])
    x = n
    while x > 0:
        digit = x % 10
        A.insertFirst(digit)
        x = x // 10
    return A
      
        
            
a  = stores_digits(241154)
print(a)