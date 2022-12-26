from collections import Counter
class Solution:
    
    def minSteps(self, s: str, t: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(t)
        diff = 0
        
        for i in range(26):
            diff += abs(sCounter[chr(97+i)] - tCounter[chr(97+i)])
        
        return diff//2