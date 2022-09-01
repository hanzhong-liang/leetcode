# import numpy as np
# import time 
# # 邻接矩阵
# inf = 1000
# w = np.array([[0, 12, inf, inf, inf, 16, 14],
#               [12, 0, 10, inf, inf, 7, inf],
#               [inf, 10, 0, 3, 5, 6, inf],
#               [inf, inf, 3, 0, 4, inf, inf],
#               [inf, inf, 5, 4, 0, 2, 8],
#               [16, 7, 6, inf, 2, 0, 9],
#               [14, inf, inf, inf, 8, 9, 0]])
# # 维度
# dim = len(w[0])
# #-------------初始化--------------------------------
# nodes = range(dim)
# # U_pre = [[] for _ in range(dim)]
# # S_pre = [[] for _ in range(dim)]
# U_pre = [0 for _ in range(dim)]
# dis = [inf,inf,inf,inf]
# # 表示已经搜索节点的距离
# S = [0 for i in range(dim)]
# # 表示还未搜索到节点的距离
# U = [inf for i in range(dim)]
# # 已经搜索到的节点列表
# searched_node = []

# #--------------开始搜索-------------------------------
# node = 3
# start = time.time()
# while len(searched_node)!= dim: 
#     # 在新节点的基础上更新距离
#     dis = [inf for i in range(dim)]
#     for i in range(dim):
#         if i not in searched_node and w [node,i] != inf:
#         # if i not in searched_node:
#             # 新距离 = 已知最短距离 + 新节点搜索的距离
#             dis [i] = w [node,i] + S[node]
#             # 比较新距离与旧距离之间的大小关系
#             if dis[i] <= U[i]:
#                 U[i] = dis[i]
#                 U_pre[i] = U_pre[node]+1
#             # if dis[i] == S[i]:
#             #     U_pre[i] += U_pre[node]
#     new_node = U.index(min(U))
#     S[new_node] = min(U)
#     # 已经搜索到的U值无穷大
#     U[new_node] = inf
#     searched_node.append(new_node)
#     node = new_node
# end = time.time()
# print(S)
# print(end-start)
# print(U_pre)


import numpy as np
import time 
# 邻接矩阵
inf = 1000
w = np.array([[0, 12, inf, inf, inf, 16, 14],
              [12, 0, 10, inf, inf, 7, inf],
              [inf, 10, 0, 3, 5, 6, inf],
              [inf, inf, 3, 0, 4, inf, inf],
              [inf, inf, 5, 4, 0, 2, 8],
              [16, 7, 6, inf, 2, 0, 9],
              [14, inf, inf, inf, 8, 9, 0]])
# 维度
dim = len(w[0])
#-------------初始化--------------------------------
nodes = range(dim)
U_pre = [[_] for _ in range(dim)]
S_pre = [[] for _ in range(dim)]
dis = [inf,inf,inf,inf]
# 表示已经搜索节点的距离
S = [0 for i in range(dim)]
# 表示还未搜索到节点的距离
U = [inf for i in range(dim)]
# 已经搜索到的节点列表
searched_node = []

#--------------开始搜索-------------------------------
node = 3
start = time.time()
while len(searched_node)!= dim: 
    # 在新节点的基础上更新距离
    dis = [inf for i in range(dim)]
    for i in range(dim):
        if i not in searched_node and w [node,i] != inf:
        # if i not in searched_node:
            # 新距离 = 已知最短距离 + 新节点搜索的距离
            dis [i] = w [node,i] + S[node]
            # 比较新距离与旧距离之间的大小关系
            if dis[i] <= U[i]:
                U[i] = dis[i]
                U_pre[i]=[i]+U_pre[node]
    new_node = U.index(min(U))
    S[new_node] = min(U)
    # 已经搜索到的U值无穷大
    U[new_node] = inf
    searched_node.append(new_node)
    node = new_node
end = time.time()
print(S)
print(end-start)
print(U_pre[0])
