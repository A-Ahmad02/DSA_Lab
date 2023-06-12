# -*- coding: utf-8 -*-
"""
Experiment 10
Question 1

"""

def try_to_relax(Adj, w, Nw, d, parent, u, v):
    if d[v] > d[u] + w[u][v] + Nw[u]:           # better path through vertex u
        d[v] = d[u] + w[u][v] + Nw[u]          # relax edge with shorter path found
        parent[v] = u

class PriorityQueue:                # Hash Table Implementation
    def __init__(self):             # stores keys with unique labels
        self.A = {}
    def insert(self, label, key):   # insert labeled key
        self.A[label] = key
    def extract_min(self):          # return a label with minimum key
        min_label = None
        for label in self.A:
            if (min_label is None) or (self.A[label] < self.A[min_label]):
                min_label = label
        del self.A[min_label]
        return min_label
    def decrease_key(self, label, key): # decrease key of a given label
        if (label in self.A) and (key < self.A[label]):
            self.A[label] = key

def dijkstra(Adj, w, Nw, s):
    d = [float('inf') for _ in Adj]     # shortest path estimates d(s, v)
    parent = [None for _ in Adj]        # initialize parent pointers
    d[s], parent[s] = 0, s              # initialize source
    Q = PriorityQueue()                 # initialize empty priority queue
    V = len(Adj)                        # number of vertices
    for v in range(V):                  # loop through vertices
        Q.insert(v, d[v])               # insert vertex-estimate pair
    for _ in range(V):                  # main loop
        u = Q.extract_min()             # extract vertex with min estimate
        for v in Adj[u]:                # loop through out-going edges
            try_to_relax(Adj, w, Nw, d, parent, u, v)
            Q.decrease_key(v, d[v])     # update key of vertex
    return d, parent

Adj =  [[0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0]]
        
G = {i:[] for i in range(len(Adj))}
for i in range(len(Adj)):
    for j in range(len(Adj[i])):
        if Adj[i][j]:
            G[i].append(j)
# print(G)

w =[[0, 10, 0, 3, 0],
    [0, 0, 2, 1, 0],
    [0, 0, 0, 0, 7],
    [0, 4, 8, 0, 2],
    [0, 0, 5, 0, 0]]

Nw = [0, 2, 1, 0, 0]

d, parent = dijkstra(G, w, Nw,  0)
print("Shortest paths:", d)