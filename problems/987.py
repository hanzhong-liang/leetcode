# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeDict = collections.defaultdict(list)
        res = []
        
        def dfs(node, row, col):
            if not node:
                return 
            nodeDict[col].append((row,node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root,0,0)
        
        nodeDict=sorted(nodeDict.items(),key=lambda x:x[0])
        
        for col, itemList in nodeDict:
            itemList.sort(key=lambda x: (x[0],x[1]))
            res.append([x[1] for x in itemList])
        
        return res
        # print(nodeDict)
        