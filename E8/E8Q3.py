# -*- coding: utf-8 -*-
"""
Experiment 8
Question 3

"""
def height(A):
    if A: return A.height
    else: return -1
class Binary_Node:
    def __init__(A, x): # O(1)
        A.item = x
        A.max_ = A
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
        D.max_, B.max_ = D, B
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
        D.max_, B.max_ = D, B
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
            
        A.maintain_max_1() # O(1)
        A.maintain_min_1() # O(1)
        T.tree1.root.maintain_max_1() # O(1)
        T.tree1.root.maintain_min_1() # O(1)
        
    
    def full_traverse_subtree(self): # O(n)
        if self.left:
            self.left.full_traverse_subtree()
        print(f"{self.item} {self.min_.item[1]} {self.max_.item[1]}", end=" | ") 
        if self.right:
            self.right.full_traverse_subtree()
        return
    
    
    def traverse_subtree(self): # O(n)
        if self.left:
            # print("L", end=" ")
            self.left.traverse_subtree()
        print(f"{self.item[0]}", end=" ")
        if self.right:
            # print("R", end=" ")
            self.right.traverse_subtree()
        return
    
    def find_insert(self, car): # O(log n)
        if self.item[0] >= car.item[0] and self.left == None:
            print("Car inserted")
            return self.subtree_insert_before(car)
        elif self.item[0] <= car.item[0] and self.right == None:
            print("Car inserted")
            self.subtree_insert_after(car)
            return 
        if self.item[0] > car.item[0]: return self.left.find_insert(car)
        elif self.item[0] == car.item[0]: return self.find_insert(car)
        else: return self.right.find_insert(car)
        
    def find_remove(self, car): # O(log n)
        if self.item[0] == car.item[0]:
            print("Car removed")
            return self.subtree_delete()
        elif self.left == None and self.right == None:
            print("Car not in catalogue")
            return 
        
        if self.item[0] > car.item[0]: return self.left.find_remove(car)
        elif self.item[0] == car.item[0]: return self.find_remove(car)
        else: return self.right.find_remove(car)
    
    def find_car_max_0(self, budget):   # O(log n)
        if self.min_.item[1] > budget:
            print("Car not in catalogue")
            return 
        elif self.left == None and self.right == None:
            return self
        elif self.left == None:
            if self.right.min_.item[1] <= budget: return self.right.find_car_max_0(budget)
            else: return self
        elif self.right == None:
            if  self.item[1] <= budget: return self
            else:  return self.left.find_car_max_0(budget)
        else:
            if self.right.min_.item[1] <= budget: return self.right.find_car_max_0(budget)
            elif self.item[1] <= budget: return self
            else:  return self.left.find_car_max_0(budget)
            
    def find_car_min_0(self, rel):   # O(log n)
        if self.max_.item[1] < rel:
            print("Car not in catalogue")
            return 
        elif self.left == None and self.right == None:
            return self
        elif self.left == None:
            if self.item[1] >= rel: return self
            else: return self.right.find_car_min_0(rel)
        elif self.right == None:
            if  self.left.max_.item[1] >= rel: return self.left.find_car_min_0(rel)
            else:  return self
        else:
            if self.left.max_.item[1] >= rel: return self.left.find_car_min_0(rel)
            elif self.item[1] >= rel: return self
            else:  return self.right.find_car_min_0(rel)
            
        
    def calc_max_1(self):# O(n)
        if self.left == None and self.right == None: self.max_ = self
        elif self.left == None:
            a = self.right.calc_max_1()
            if a.item[1] > self.item[1]: self.max_ = a
        elif self.right == None:
            b = self.left.calc_max_1()
            if b.item[1] > self.item[1]: self.max_ = b
        else:
            A = self.right.calc_max_1()
            B = self.left.calc_max_1()
            if A.item[1] >= self.item[1] and A.item[1] >= B.item[1]: self.max_ = A
            if B.item[1] >= self.item[1] and B.item[1] >= A.item[1]: self.max_ = B
        return self.max_
    def maintain_max_1(self): # O(1)
        if self.left == None and self.right == None: self.max_ = self
        elif self.left == None:
            if self.right.max_.item[1] > self.item[1]: self.max_ = self.right.max_
        elif self.right == None:
            if self.left.max_.item[1] > self.item[1]: self.max_ = self.left.max_
        else:
            A = self.right.max_
            B = self.left.max_
            if A.item[1] >= self.item[1] and A.item[1] >= B.item[1]: self.max_ = A
            if B.item[1] >= self.item[1] and B.item[1] >= A.item[1]:self.max_ = B
    def calc_min_1(self):# O(n)
        if self.left == None and self.right == None: self.min_ = self
        elif self.left == None:
            a = self.right.calc_min_1()
            if a.item[1] < self.item[1]: self.min_ = a
        elif self.right == None:
            b = self.left.calc_min_1()
            if b.item[1] < self.item[1]: self.min_ = b
        else:
            A = self.right.calc_min_1()
            B = self.left.calc_min_1()
            if A.item[1] <= self.item[1] and A.item[1] <= B.item[1]: self.min_ = A
            if B.item[1] <= self.item[1] and B.item[1] <= A.item[1]: self.min_ = B
        return self.min_
    def maintain_min_1(self): # O(1)
        if self.left == None and self.right == None: self.min_ = self
        elif self.left == None:
            if self.right.min_.item[1] < self.item[1]: self.min_ = self.right.min_
        elif self.right == None:
            if self.left.min_.item[1] < self.item[1]: self.min_ = self.left.min_
        else:
            A = self.right.min_
            B = self.left.min_
            if A.item[1] <= self.item[1] and A.item[1] <= B.item[1]: self.min_ = A
            if B.item[1] <= self.item[1] and B.item[1] <= A.item[1]: self.min_ = B
                
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
        self.root.calc_max_1()
        self.root.calc_min_1()

class List_Binary_Tree():
    def __init__(L, Tree_Type = Binary_Tree):
        L.tree1 = None
        L.tree2 = None
        L.size = 0
        L.Tree_Type = Tree_Type
    def __len__(T): return T.size
    def build(L,X):
        L.size = len(X)
        L.tree1 = Binary_Tree()
        L.tree2 = Binary_Tree()
        X2 = []
        for i in range(len(X)):
            X2.append((X[i][1],X[i][0]))
        L.tree1.build(X)
        L.tree2.build(X2)

    def traversal_order(L):
        print("Traversal order: Tree1: ", end="")
        L.tree1.root.traverse_subtree()
        print("\t Tree2: ", end="")
        L.tree2.root.traverse_subtree()
        print()
    
    def buy(L,car): # adds a car to the inventory
        car2 = Binary_Node((car.item[1],car.item[0]))
        L.tree1.root.find_insert(car)
        L.tree2.root.find_insert(car2)
          
    def sell(L,car): # removes the car from the inventory
        car2 = Binary_Node((car.item[1],car.item[0]))
        L.tree1.root.find_remove(car)
        L.tree2.root.find_remove(car2)
        
    def find_car(L,budget): # which gives you the most reliable car within your budget i.e. the most reliable car with price ≤ budget
        return L.tree2.root.find_car_max_0(budget)
    
    def car_options(L, reliability): #which finds for you the cheapest car that has a reliability ≥ reliability
        return L.tree1.root.find_car_min_0(reliability)
    
T = List_Binary_Tree()
X = [(1,1),(2,4),(5,6),(7,8),(9,0),(10,10)]

T.build(X)
print("Size: ",T.size)
T.traversal_order()
T.tree1.root.full_traverse_subtree()
print("\n")

car = Binary_Node((6,5))
T.buy(car)
T.traversal_order()
T.tree1.root.full_traverse_subtree()
print("\n")

T.sell(car)
T.traversal_order()
T.tree2.root.full_traverse_subtree()
print("\n")

budget = 9
print(f"The best car in {budget}M is {T.find_car(budget)}")
T.tree2.root.full_traverse_subtree()
print("\n")

reliability = 9 
print(f"The best car above reliability {reliability} is {T.car_options(reliability)}")
T.tree1.root.full_traverse_subtree()
print("\n")