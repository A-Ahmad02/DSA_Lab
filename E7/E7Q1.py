# -*- coding: utf-8 -*-
"""
Experiment 7
Question 1

"""

class Binary_Node():
    def __init__(A, x, label=None): # O(1)
        A.item = x
        A.label = label
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update() # wait for R07!
    def subtree_iter(A): # O(n)
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()
    def subtree_first(A): # O(h)
        if A.left: return A.left.subtree_first()
        else: return A
    def subtree_last(A): # O(h)
        if A.right: return A.right.subtree_last()
        else: return A
    def successor(A): # O(h)
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent
    def predecessor(A): # O(h)
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    def subtree_insert_before(A, B): # O(h)
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
            # A.maintain() # wait for R07!
    def subtree_insert_after(A, B): # O(h)
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
            # A.maintain() # wait for R07!
    def subtree_delete(A): # O(h)
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
            # A.parent.maintain() # wait for R07!
        return A
    def traverse_subtree(self):
        if self.left:
            self.left.traverse_subtree()
        print(self.item, end=" ")
        if self.right:
            self.right.traverse_subtree()
        return
       
        
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
    

def traversal_order(T):
    node = T.root
    node.traverse_subtree()
    print()
    
T = Binary_Tree()
X = ["F","K","D","J","H","I","B","E","A","G","C"]
T.build(X)
print("Size: ",T.size)
print("Traversal order: ", end="")
traversal_order(T)