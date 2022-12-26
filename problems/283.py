# 最经典的移动零的题

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        n = len(nums)
        
        for num in nums:
            if num!=0:
                nums[l]=num
                l+=1
                
        for i in range(l,n):
            nums[i] = 0
        