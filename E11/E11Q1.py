# -*- coding: utf-8 -*-
"""
Experiment 11
Question 1

"""
from random import randint

class Item:
    def __init__(self, x): # O(1)
        self.key = x
        self.value = randint(1,100)


# class Linked_List_Node:
#     def __init__(self, x): # O(1)
#         self.item = x
#         self.next = None
#     def later_node(self, i): # O(i)
#         if i == 0: return self
#         assert self.next
#         return self.next.later_node(i - 1)

# class Linked_List_Seq:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#     def __len__(self): return self.size
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node.item
#             node = node.next
#     def build(self, X):
#         for a in reversed(X):
#             self.insert_first(a)
#     def get_at(self, i):
#         node = self.head.later_node(i)
#         return node.item
#     def set_at(self, i, x): # O(i)
#         node = self.head.later_node(i)
#         node.item = x
#     def insert_first(self, x): # O(1)
#         new_node = Linked_List_Node(x)
#         new_node.next = self.head
#         self.head = new_node
#         self.size += 1
#     def delete_first(self): # O(1)
#         x = self.head.item
#         self.head = self.head.next
#         self.size -= 1
#         return x
#     def insert_at(self, i, x): # O(i)
#         if i == 0:
#             self.insert_first(x)
#             return
#         new_node = Linked_List_Node(x)
#         node = self.head.later_node(i - 1)
#         new_node.next = node.next
#         node.next = new_node
#         self.size += 1
#     def delete_at(self, i): # O(i)
#         if i == 0:
#             return self.delete_first()
#         node = self.head.later_node(i - 1)
#         x = node.next.item
#         node.next = node.next.next
#         self.size -= 1
#         return x
#     # O(n)
#     def insert_last(self, x): self.insert_at(len(self), x)
#     def delete_last(self): return self.delete_at(len(self) - 1)

# def Set_from_Seq(seq):
#     class set_from_seq:
#         def __init__(self): self.S = seq()
#         def __len__(self): return len(self.S)
#         def __iter__(self): yield from self.S
#         def build(self, A):
#             self.S.build(A)
#         def insert(self, x):
#             for i in range(len(self.S)):
#                 if self.S.get_at(i).key == x.key:
#                     self.S.set_at(i, x)
#                     return
#             self.S.insert_last(x)
#         def delete(self, k):
#             for i in range(len(self.S)):
#                 if self.S.get_at(i).key == k:
#                     return self.S.delete_at(i)
#         def find(self, k):
#             for x in self:
#                 if x.key == k: return x
#             return None
#         def find_min(self):
#             out = None
#             for x in self:
#                 if (out is None) or (x.key < out.key):
#                     out = x
#             return out
#         def find_max(self):
#             out = None
#             for x in self:
#                 if (out is None) or (x.key > out.key):
#                     out = x
#             return out
#         def find_next(self, k):
#             out = None
#             for x in self:
#                 if x.key > k:
#                     if (out is None) or (x.key < out.key):
#                         out = x
#             return out
#         def find_prev(self, k):
#             out = None
#             for x in self:
#                 if x.key < k:
#                     if (out is None) or (x.key > out.key):
#                         out = x
#             return out
#         def iter_ord(self):
#             x = self.find_min()
#             while x:
#                 yield x
#                 x = self.find_next(x.key)
#     return set_from_seq

class Hash_Table_Set:
    def __init__(self, r = 200): # O(1)
        # self.chain_set = Set_from_Seq(Linked_List_Seq)
        self.A = [None]
        self.size = 0
        self.r = r # 100/self.r = fill ratio
        self.p = 2**31 - 1
        self.a = randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(1)
    def __len__(self): return self.size # O(1)
    def __iter__(self): # O(n)
        for X in self.A:
            yield X
    def build(self, X): # O(n)e
        for x in X: self.insert(x)
    def _hash(self, k, m): # O(1)
        return ((self.a * k) % self.p) % m
    def _compute_bounds(self): # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) * 100*100 // (self.r*self.r)
    def _resize(self, n): # O(n)
        if (self.lower >= n) or (n >= self.upper) or len(self.A)*0.66 < self.size:
            f = self.r // 100
            if self.r % 100: f += 1
            # f = ceil(r / 100)
            m = max(n, 1) * f
            # A = [self.chain_set() for _ in range(m)]
            A = [None  for _ in range(m)]
            for x in self.A:
                if x != None and x != "del":
                    h = self._hash(x.key, m)
                    if A[h] != None:
                        h = self.Linear_Probing(h,A,m,0)
                    A[h] = x
            self.A = A
            self._compute_bounds()
            
    def find(self, k): # O(1)e
        h = self._hash(k, len(self.A))
        if self.A[h] == None:
            return None, None
        elif self.A[h].key == k: return self.A[h], h
        else: 
            i = 0
            while i<len(self.A):
                i+=1
                h = (h + i) % len(self.A)
                if self.A[h] == None: return None, None
                if self.A[h].key == k: break
            if self.A[h].key == k: return self.A[h], h
            else: return None, None
        
                
    def insert(self, x): # O(1)ae
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        if self.A[h] is None: pass
        else: h = self.Linear_Probing(h)
        self.A[h] = x
        self.size += 1
    
    def delete(self, k): # O(1)ae
        assert len(self) > 0
        _ , h = self.find(k)
        if h == None: return
        self.A[h] = "del"
        self.size -= 1
        self._resize(self.size)
        
    def find_min(self): # O(n)
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out
    def find_max(self): # O(n)
        out = None
        for x in self:
            if (out is None) or (x.key > out.key):
                out = x
        return out
    def find_next(self, k): # O(n)
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out
    def find_prev(self, k): # O(n)
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out
    def iter_order(self): # O(nˆ2)
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)
            
    def Linear_Probing(self, h, A=None, m=None, i=0):
        if m == None: m = len(self.A)
        if A == None: A = self.A
        if A[h] == None or A[h] == "del" : return h
        h_ = (h + i) % m
        return self.Linear_Probing(h_, A, m, i+1)
    
    def __str__(self):
        str_ =""
        for i in self.A:
            if i != None and i != "del" :
                str_ += str(i.key) +" "
            elif i == "del" :
                str_ += i +" "
                
            else:
                str_ += "None "
        return str_
        
h = Hash_Table_Set()
h.build([Item(j)  for j in range(15)])
# print(h.find(3))
# print("Hashtable: ", h)
# print("Filled/Size: ",h.size,"/" ,len(h.A))
h.delete(9)
print("Hashtable: ", h)
print("Filled/Size: ",h.size,"/" ,len(h.A))

        