# -*- coding: utf-8 -*-
"""
Experiment 9
Question 2

"""

def bfs(Adj, s): # Adj: adjacency list, s: starting vertex
    parent = [None for v in Adj] # O(V) (use hash if unlabeled)
    parent[s] = s # O(1) root
    level = [[s]] # O(1) initialize levels
    while 0 < len(level[-1]): # O(?) last level contains vertices
        level.append([]) # O(1) amortized, make new level
        print(end=" -> ")
        for u in level[-2]: # O(?) loop over last full level
            print(u, end=" ")
            for v in Adj[u]: # O(Adj[u]) loop over neighbors
                if parent[v] is None: # O(1) parent not yet assigned
                    parent[v] = u # O(1) assign parent from level[-2]
                    level[-1].append(v) # O(1) amortized, add to border
    
    print()
    return parent

def dfs(Adj, s, parent = None, order = None): # Adj: adjacency list, s: start
    if parent is None: # O(1) initialize parent list
        parent = [None for v in Adj] # O(V) (use hash if unlabeled)
        parent[s] = s # O(1) root
        order = [] # O(1) initialize order array
    print(end=" -> ")
    for v in Adj[s]: # O(Adj[s]) loop over neighbors
        if parent[v] is None: # O(1) parent not yet assigned
            parent[v] = s # O(1) assign parent
            dfs(Adj, v, parent, order) # Recursive call
        print(Adj[s], end="\n")
    
    order.append(s) # O(1) amortized
    return parent, order

def full_dfs(Adj): # Adj: adjacency list
    parent = [None for v in Adj] # O(V) (use hash if unlabeled)
    order = [] # O(1) initialize order list
    for v in range(len(Adj)): # O(V) loop over vertices
        if parent[v] is None: # O(1) parent not yet assigned
            parent[v] = v # O(1) assign self as parent (a root)
            dfs(Adj, v, parent, order) # DFS from v (BFS can also be used)
    return parent, order

Adj = [[0, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0]]
# G = {}
# for i in range(len(Adj)):
#     G[i] = []
#     for j in range(len(Adj[i])):
#             G[i].append(j)
        
""" Part B """
G = {i:[] for i in range(len(Adj))}
for i in range(len(Adj)):
    for j in range(len(Adj[i])):
        if Adj[i][j]:
            G[i].append(j)

print(G)

""" Part C """

# Adj_L = []
# for i in G:
#     Adj_L.append(G[i])
# print(Adj_L)

print("BFS",bfs(G, 0))

""" Part D """

print("DFS",dfs(Adj, 0))