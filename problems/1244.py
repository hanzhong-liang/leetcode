# heap 需要掌握这些
# heapq.heappush(heap,x)
# heapq.heappop(heap)
                

class Leaderboard:

    def __init__(self):
        self.dict = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.dict[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        res = 0
        
        for score in self.dict.values():
            heapq.heappush(heap, score)
            if len(heap)>K:
                heapq.heappop(heap)
        
        for score in heap:
            res+=score
        
        return res
        

    def reset(self, playerId: int) -> None:
        self.dict.pop(playerId)