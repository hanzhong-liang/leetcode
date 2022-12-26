class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        smallest = float('INF')
        while l<=r:
            mid = l + (r-l)//2
            # 需要注意这个等号
            if nums[0] <= nums[mid]:
                smallest = min(nums[0],smallest)
                l = mid+1
            else:
                smallest = min(nums[mid],smallest)
                r = mid-1
        
        return smallest