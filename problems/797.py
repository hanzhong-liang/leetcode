# class Solution:
#     # 这个题可以用dfs的方式写 也可以用backtracking的方式写
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         pathList = []
#         N = len(graph)
        
#         def backtrack(index, path):
#             if index == N-1:
#                 pathList.append(path[:])
#                 return
#             for i in graph[index]:
#                 path.append(i)
#                 backtrack(i,path)
#                 path.pop()
                
#         backtrack(0,[0])
#         return pathList

def allPathsSourceTarget(graph):
    result = []
    N = len(graph)
    
    def backtracking(path, index):
        if index == N-1:
            result.append(path[:])
            return
        for node in graph[index]:
            path.append(node)
            backtracking(path,node)
            path.pop()

    backtracking([0],0)
    return result
ch = 'a'
if ch.isnumeric():
    print(1)