# -*- coding: utf-8 -*-
"""
Experiment 8
Question 1

"""
def height(A):
    if A: return A.height
    else: return -1
class Binary_Node:
    def __init__(A, x): # O(1)
        A.item = x
        A.sum = x
        A.size = 1
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
            A.sum, B.sum = B.sum, A.sum
            A.size, B.size = B.size, A.size
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
        D.sum, B.sum = B.sum, D.sum
        D.size, B.size = B.size, D.size
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
        B.sum, D.sum = D.sum, B.sum
        B.size, D.size = D.size, B.size
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
        A.maintain_sum() # O(1)
        A.maintain_size() # O(1)
        if A.parent: A.parent.maintain()
        
    
    def full_traverse_subtree(self): # O(n)
        if self.left:
            self.left.full_traverse_subtree()
        print(f"{self.item} {self.sum} {self.size}", end=" | ")
        if self.right:
            self.right.full_traverse_subtree()
        return
    
    
    def traverse_subtree(self): # O(n)
        if self.left:
            self.left.traverse_subtree()
        print(f"{self.item}", end=" ")
        if self.right:
            self.right.traverse_subtree()
        return
    
    def subtree_size(self): # O(n)
        if self.left == None and self.right == None:
            self.size = 1
        elif self.left == None and self.right != None:
            self.size = 1 + self.right.subtree_size()
        elif self.left != None and self.right == None:
            self.size = 1 + self.left.subtree_size()
        else:
            self.size = 1 + self.left.subtree_size() + self.right.subtree_size()
        return self.size
    
    def subtree_mean(self):   # O(1)   
        # print(f"P= {self.item}M R= {self.sum} S= {self.size}")
        print(f"{self.sum/self.size:.2f}")
        return
            
    def calc_sum(self):# O(n)
        if self.left == None and self.right == None:
            self.sum = self.item
        elif self.left == None and self.right != None:
            self.sum = self.right.calc_sum() + self.item
        elif self.left != None and self.right == None:
            self.sum = self.left.calc_sum() + self.item
        else:
            A = self.right.calc_sum()
            B = self.left.calc_sum()
            self.sum = A + B + self.item
        return self.sum
    
    def maintain_sum(self): # O(1)
        if self.left == None and self.right == None:
            self.sum = self.item
        elif self.left == None and self.right != None:
            self.sum = self.right.sum + self.item
        elif self.left != None and self.right == None:
            self.sum = self.left.sum + self.item
        else:
            self.sum = self.right.sum + self.left.sum + self.item
        return
    
    def maintain_size(self): # O(1)
        if self.left == None and self.right == None:
            self.size = 1
        elif self.left == None and self.right != None:
            self.size = self.right.size + 1
        elif self.left != None and self.right == None:
            self.size = self.left.size + 1
        else:
            self.size = self.right.size + self.left.size + 1
        return
            
                
    def __str__(self):
        return f" P= {self.item}M R= {self.rel}"
        
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
    def __init__(T, Node_Type = Size_Node):
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
        self.root.calc_sum()
        self.root.subtree_size()

def traversal_order(T):
    T.root.traverse_subtree()
    print()
    
        
X = [1,2,5,7,9,10]

T = Binary_Tree()
T.build(X)
print("Size of tree: ",T.size)
print("Traversal order: ", end="")
traversal_order(T)
T.root.full_traverse_subtree()
print("\nMean of subtree is ", end="")
T.root.subtree_mean()