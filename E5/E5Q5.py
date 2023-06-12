# -*- coding: utf-8 -*-
"""
Experiment 5
Question 5

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
            self.tail = None
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
        new = Node(x)
        if (self.tail and self.head) == None:
            self.head = new
            self.tail = new
        else:
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
            
# def two_list(A,B):
#     C = []
#     for i in range(len(A)):
#         for j in range(B[i]):
#             C.append(A[i])
#     return LinkedList(C)

            
def two_list(A,B):
    C = LinkedList([])
    for i in range(len(A)):
        for j in range(B[i]):
            C.insertLast(A[i])
    return C
            
# def two_list(A,B):
#     C = []
#     for i in range(len(A)):
#         C = C + ( [A[i]]* B[i])
#     return LinkedList(C)

A = [1,12,4,15,2]
B = [1,2,4,1,0]
print(two_list(A,B))