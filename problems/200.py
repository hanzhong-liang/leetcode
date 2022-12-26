# bfs 在append到q之后 就要立刻visited改状态
# 否则同一层的点有可能会又判断到 
# 嗷嗷这就是为什么visited要用set吧哈哈哈原来是这样啊

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    q = collections.deque()
                    ans+=1
                    q.append((i,j))
                    grid[i][j] = '0'
                    while q:
                        x,y=q.popleft()
                        for xi,yi in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                            if -1<xi<n and -1<yi<m and grid[xi][yi] == '1':
                                grid[xi][yi]='0'
                                q.append((xi,yi))
        return ans
    
#     def dfs(self, grid, row, col, rl, cl):
#         if row < 0 or row >= rl or col < 0 or col >= cl or grid[row][col] != "1":
#             return
#         grid[row][col] = "2"
#         self.dfs(grid, row + 1, col, rl, cl)
#         self.dfs(grid, row, col + 1, rl, cl)
#         self.dfs(grid, row - 1, col, rl, cl)
#         self.dfs(grid, row, col - 1, rl, cl)

#     def numIslands(self, grid: List[List[str]]) -> int:
#         rl = len(grid)
#         cl = len(grid[0])
#         islands = 0

#         for row in range(rl):
#             for col in range(cl) :
#                 if grid[row][col] == "1":
#                     self.dfs(grid, row, col, rl, cl)
#                     islands += 1
#         return islands
                                
                    
        