class Solution:
    # n^2 会TLE
    # 需要用贪心的方法去做

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp_table = [1 for i in range(n)]
    #     for i in range(1,n):
    #         for j in range(0,i):
    #             if nums[j]<nums[i]:
    #                 dp_table[i] = max(dp_table[i],dp_table[j]+1)
        
        
    #     return max(dp_table)

    # 这个题用了贪心的思路
    # 可以不更新最大长度 因为len(res) 就是曾经到达过的最大长度

    def lengthOfLIS(self, nums: List[int]) -> int:
        def binsearchleft(val):
            n = len(res)
            l,r=0,n-1
            while l<=r:
                mid = (l+r) //2
                if res[mid] == val:
                    return mid
                if res[mid]<val:
                    l = mid+1
                else:
                    r = mid-1
            return l
        
        res = [nums[0]]
        n = len(nums)
        
        for num in nums:
            if num>res[-1]:
                res.append(num)
            else:
                index = binsearchleft(num)
                res[index] = num
                
        return len(res)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        n = len(nums)
        
        for num in nums:
            if num>res[-1]:
                res.append(num)
            else:
                index = bisect.bisect_left(res, num)
                res[index] = num
                
        return len(res)
        