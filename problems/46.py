# time O(n!) factorial
# space O(n)
class Solution:
    # 这是一个很巧妙的回溯，有效降低时间复杂度
    # 改变nums里面的顺序，前index个数就是已经排列好的
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def backtracking(index):
            if index == n:
                result.append(nums[:])
                return 
            
            for i in range(index,n):
                nums[i],nums[index]=nums[index],nums[i]
                backtracking(index+1)
                nums[i],nums[index]=nums[index],nums[i]
        
        backtracking(0)
        return result