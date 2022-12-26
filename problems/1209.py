class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = [] #[ch,k]
        res = ""
        for ch in s:
            if stack and ch == stack[-1][0]:
                stack[-1][1]+=1
            else:
                stack.append([ch,1])
            
            if stack[-1][1] == k:
                stack.pop()

        
        for item in stack:
            res = res+item[0]*item[1]
            
        return res