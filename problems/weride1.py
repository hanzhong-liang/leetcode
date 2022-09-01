import numpy as np
from collections import deque
import copy

# 邻接矩阵
inf = float('inf')
w = np.array([[0, 12, inf, inf, inf, 16, 14],
              [12, 0, 10, inf, inf, 7, inf],
              [inf, 10, 0, 3, 5, 6, inf],
              [inf, inf, 3, 0, 4, inf, inf],
              [inf, inf, 5, 4, 0, 2, 8],
              [16, 7, 6, inf, 2, 0, 9],
              [14, inf, inf, inf, 8, 9, 0]])

w = np.array([[0, 1, inf, inf, inf, 1],
              [1, 0, 2, 1, inf, inf],
              [inf, 2, 0, inf, inf, 2],
              [inf, 1, inf, 0, 1, 1],
              [inf, inf, 2, 1, 0, inf],
              [1, inf, 2, 1, inf, 0],])
start = 1
N = len(w)
q=deque([start])
cost = [inf for i in range(N)]
cost[start] = 0
visited = set()
predecessors = [set([start]) for i in range(N)]

while q:
    node = q.popleft()
    for i in range(N):
        if w[i][node]!=inf:
            node_cost = cost[node]+w[i][node]
            if node_cost < cost[i]:
                cost[i] = node_cost
                predecessors[i]=copy.deepcopy(predecessors[node])
                predecessors[i].add(i)
            elif node_cost == cost[i]:
                predecessors[i]=predecessors[i] | predecessors[node]
                predecessors[i].add(i)
        if i not in visited:
            q.append(i)
    visited.add(node)
print(cost)
print(predecessors)

# a = set([1,2,3])
# b = a
# a.add(4)
# print(b)
