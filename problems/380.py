# 记住choice随机选一个
# 通过建立一个dict 使查询的复杂度变为O(1)
# 通过交换位置删除最后一个 使删除的复杂度变为O(1)

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            val_index = self.dict[val]
            last = self.list[-1]

            self.dict[last],self.list[val_index]=val_index,last
            self.list.pop()
            self.dict.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()