# -*- coding: utf-8 -*-
"""
Experiment 4
Question 4

"""

class Node():
    def __init__(self,data,nextNode=None,prevNode=None):
        self.data = int(data)
        self.next = nextNode
        self.prev = prevNode

class DoublyLinkedList():
    def __init__(self,A):
        if A == []:
            A.append(int(input("Please enter 1st element:  ")))
        self.head = Node(A[0])
        self.length = len(A)
        
        old = self.head
        for i in range(1,self.length,1):
            new = Node(A[i])
            old.next = new
            new.prev = old
            old = new
            
        self.tail = old
    
    def insertFirst(self,x):
        new = Node(x)
        self.head.prev = new
        new.next = self.head
        self.head = new
    
    def deleteFirst(self):
        
        newhead = self.head.next
        self.head = newhead
        self.head.prev = None
        
    
    def insertLast(self,x):
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
                
    def __call__(self):
        return "LinkedList"
        
    def __str__(self):
        k = self.head
        string = str(k.data)
        while k.next:
            k = k.next
            string += (", "+str(k.data))
        return "["+string+"]"

    
a  = DoublyLinkedList([31,24,12,8,2,1,100])

a.insertFirst(3)
print("Insert First:",a)
a.insertLast(51)
print("Insert Last:",a)
a.deleteFirst()
print("Delete First:",a)
a.deleteLast()
print("Delete Last:",a)
