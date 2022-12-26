class OrderedStream(object):
    
    def __init__(self, n):
        self.ans = [""]*(n+1)
        self.idx = 0

    def insert(self, idKey, value):
        self.ans[idKey - 1] = value

        res = []

        while self.ans[self.idx]:
            res.append(self.ans[self.idx])
            self.idx += 1

        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)