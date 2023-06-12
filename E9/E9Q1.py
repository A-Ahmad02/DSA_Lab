# -*- coding: utf-8 -*-
"""
Experiment 9
Question 1

"""
V = 4
inp=[[0,1],[1,2],[1,3],[2,3],[3,0]]


L = {i:"" for i in range(V)}

for i in inp:
    L[i[0]] += str(i[1]) + " "
for j in L:
    print(j,"->",L[j])