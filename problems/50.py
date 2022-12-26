# 这个题注意 -1的情况就行
class Solution:
    def myPow(self, x: float, n: int) -> float:
        cur = 1
        final=1
        val=x
        sign = 1 if n>=0 else -1
        n = abs(n)
        
        while n>0:
            while cur*2<=n:
                cur=cur*2
                val=val*val
            n-=cur
            final=final*val
            cur=1
            val=x
        
        
            
        return final if sign==1 else 1/final