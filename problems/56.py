# time O(nlogn)
# space O(n)
# 先排序 再合并 如果合并不进去 就是一个新的interval
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0],x[1]))
        mergedIntervals=[[-2,-1]]
        for interval in intervals:
            if interval[0]>mergedIntervals[-1][1]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1],interval[1])
        
        return mergedIntervals[1:]