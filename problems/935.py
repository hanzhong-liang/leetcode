class Solution:
    possibleMove = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,9],[1,3],[2,4]]
    
    def knightDialer(self, n: int) -> int:
        M = 1000000007
        dp_table = [[0]*(n+1) for _ in range(10)]
        for i in range(10):
            dp_table[i][1]=1
        for j in range(2,n+1):
            for i in range(10):
                for nxt in self.possibleMove[i]:
                    dp_table[i][j] += dp_table[nxt][j-1]
        
        return sum([dp_table[i][n] for i in range(10)])%M

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9+7
        memo = [[1] * 10 for _ in range(n)]
        
        transitions = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        for step in range(1, n):
            for num in range(10):
                combos = 0
                for jump in transitions[num]:
                    combos += memo[step - 1][jump]
                memo[step][num] = combos % MOD
        
        return sum(memo[-1]) % MOD