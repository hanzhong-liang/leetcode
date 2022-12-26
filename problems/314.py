# 树不一定 非要 dfs
# bfs能够保证层序 可能会更好一点
# 字典排序 res = sorted(res.items(), key=lambda x: x[0])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = collections.defaultdict(list)
        q = collections.deque()
        q.append((root,0))
        
        while q:
            node,col = q.popleft()
            
            res[col].append(node.val)
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        
        
        res = sorted(res.items(), key=lambda x: x[0])
        return [item[1] for item in res]