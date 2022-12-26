# 二分 一定有一半有序 一半无序
# 在有序里找不到 就去无序里找

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r=0,n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            # 这里是大于等于
            if nums[mid]>=nums[0]:
                # 这里是大于等于 
                if nums[0]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            
            else:
                # 这里是大于等于 
                if nums[mid]<=target<=nums[-1]:
                    l=mid+1
                else:
                    r=mid-1
        
        return -1