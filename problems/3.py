# 双指针 需要想明白开闭关系 可以是左闭右闭
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCounter = defaultdict(int)
        l = 0
        n = len(s)
        longest = 0
        length = 0
        for ch in s:
            charCounter[ch]+=1
            length+=1
            while charCounter[ch]>1:
                charCounter[s[l]]-=1
                length-=1
                l+=1
            longest = max(length,longest)
            
        return longest