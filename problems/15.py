# 三数之和 双指针 一个从左往右 一个从右往左

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans

# 三指针
# 问题在于结果不能重复，需要利用严格单调递增性来解决重复的问题
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        
        for i in range(N):
            # 提前终止
            if nums[i]>0:
                continue

            # 利用严格单调递增性来解决重复的问题
            if i!=0 and nums[i] == nums[i-1]:
                continue
            
            j,k=i+1,N-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                        
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
        return res