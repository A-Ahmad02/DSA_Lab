# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:34:50 2023

@author: Lenovo
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
        if self.tail:
            self.head = self.tail
            
    
    def deleteFirst(self):
        
        self.head = self.head.next
        self.head.prev = None
        
    
    def insertLast(self,x):
        if self.tail:
            self.head = self.tail
        new = Node(x)
        self.tail.next = new
        new.prev = self.tail
        self.tail = new
     
    def deleteLast(self):
        last = self.tail.prev
        self.tail = last
        self.tail.next = None
                
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
            
    def Sum(self):
        sum_ = self.head.data
        new = self.head
        while new.next:
            new = new.next
            sum_ = sum_ + new.data
        return sum_
    


A = LinkedList([1,1,5,15,20])
print(A.Sum())