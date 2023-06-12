# -*- coding: utf-8 -*-
"""
Experiment 8
Question 2

"""

def height(A):
    if A: return A.height
    else: return -1
class Binary_Node:
    def __init__(A, x): # O(1)
        A.item = x
        A.min_ = A
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()
    def subtree_update(A): # O(1)
        A.height = 1 + max(height(A.left), height(A.right))
    def skew(A): # O(1)
        return height(A.right) - height(A.left)
    def subtree_iter(A): # O(n)
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()
    def subtree_first(A): # O(log n)
        if A.left: return A.left.subtree_first()
        else: return A
    def subtree_last(A): # O(log n)
        if A.right: return A.right.subtree_last()
        else: return A
    def successor(A): # O(log n)
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent
    def predecessor(A): # O(log n)
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    def subtree_insert_before(A, B): # O(log n)
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
            A.maintain()
    def subtree_insert_after(A, B): # O(log n)
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
            A.maintain()
    def subtree_delete(A): # O(log n)
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
            A.parent.maintain()
        return A
    def subtree_rotate_right(D): # O(1)
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        D.min_, B.min_ = D, B
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()
    def subtree_rotate_left(B): # O(1)
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.min_, B.min_ = D, B
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()
        
    def rebalance(A): # O(1)
        if A.skew() == 2:
            if A.right.skew() < 0:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() > 0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()
        
    def maintain(A): # O(log n)
        A.rebalance()
        A.subtree_update()
        if A.parent: 
            A.parent.maintain()
            
        A.maintain_min_() # O(1)
        T.tree1.root.maintain_min_() # O(1)
        
    
    def full_traverse_subtree(self): # O(n)
        if self.left:
            self.left.full_traverse_subtree()
        print(f"{self.item} {self.min_.item}", end=" | ") 
        if self.right:
            self.right.full_traverse_subtree()
        return
    
    
    def traverse_subtree(self): # O(n)
        if self.left:
            # print("L", end=" ")
            self.left.traverse_subtree()
        print(f"{self.item}", end=" ")
        if self.right:
            # print("R", end=" ")
            self.right.traverse_subtree()
        return
    
            
    def calc_min_(self):# O(n)
        if self.left == None and self.right == None: self.min_ = self
        elif self.left == None:
            a = self.right.calc_min_()
            if a.item < self.item: self.min_ = a
        elif self.right == None:
            b = self.left.calc_min_()
            if b.item < self.item: self.min_ = b
        else:
            A = self.right.calc_min_()
            B = self.left.calc_min_()
            if A.item <= self.item and A.item <= B.item: self.min_ = A
            if B.item <= self.item and B.item <= A.item: self.min_ = B
        return self.min_
    
    def maintain_min_(self): # O(1)
        if self.left == None and self.right == None: self.min_ = self
        elif self.left == None:
            if self.right.min_.item < self.item: self.min_ = self.right.min_
        elif self.right == None:
            if self.left.min_.item < self.item: self.min_ = self.left.min_
        else:
            A = self.right.min_
            B = self.left.min_
            if A.item <= self.item and A.item <= B.item: self.min_ = A
            if B.item <= self.item and B.item <= A.item: self.min_ = B
                
    def find_watch(self, p, track=[]):
        check = self.item < p
        if check:
            track.append(self)
        if self.item == p:
            return self.predecessor()
        
        if self.left == None and self.right == None:
            if self.item < p: return self
            else: return track[-1]        # <<<---
        elif self.left == None:
            if self.item < p: return self.right.find_watch(p)
            else: return self
        elif self.right == None:
            if self.item < p: return self
            else: return self.left.find_watch(p)
        else:
            if self.item < p: return self.right.find_watch(p)
            else: return self.left.find_watch(p)
            
            
    def __str__(self):
        return f"{self.item}"
        
class Size_Node(Binary_Node):
    def subtree_update(A): # O(1)
        super().subtree_update()
        A.size = 1
        if A.left: A.size += A.left.size
        if A.right: A.size += A.right.size
    def subtree_at(A, i): # O(h)
        assert 0 <= i
        if A.left: L_size = A.left.size
        else: L_size = 0
        if i < L_size: return A.left.subtree_at(i)
        elif i > L_size: return A.right.subtree_at(i - L_size - 1)
        else: return A
        

class Binary_Tree():
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type
    def __len__(T): return T.size
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item
    def tree_iter(T):
        node = T.subtree_first()
        while node:
            yield node
            node = node.successor()
    
    def build(self,X):
        A = [x for x in X]
        A.sort()
        self.size = len(A)
        def build_subtree(A, i, j):
            c = (i + j) // 2
            root = self.Node_Type(A[c])
            if i < c: # needs to store more items in left subtree
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c < j: # needs to store more items in right subtree
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            return root
        print()
        self.root = build_subtree(A, 0, len(A)-1)
        self.root.calc_min_()


def traversal_order(T):
    node = T.root
    node.traverse_subtree()
    print()
    # node.full_traverse_subtree()
    # print()
    

def find_k_watches(T,p,k):
    print(f"For watches with price less than {p}:", end=" ")
    node = T.root.find_watch(p)
    list_k = []
    if node == None:
        print("No matches") 
        return
    else:
        for i in range(k):
            if node == None:
                print(f"Only {i} matches")
                break
            else:
                list_k.append(node.item)
            node = node.predecessor()
    print(list_k)
            
T = Binary_Tree()
X = [1,7,9,2,3,10,5,20]
T.build(X) # Builds Tree in ascending 
print("Size: ",T.size)
print("Traversal order: ", end="")
traversal_order(T)

find_k_watches(T,11,2)
