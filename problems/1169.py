class Solution:
    # 非常之tricky的edge case
    # 如果出现两个完全一样的transanction，但是她们index不一样，算作两个
    # 存储index 而不要存储内容
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        transDict = defaultdict(set)
        
        for i, t in enumerate(transactions):
            name, time, amount, place = t.split(",")
            
            amount = int(amount)
            time = int(time)
            
            if amount>1000:
                invalid.add(i)
            
            for j,t,p in transDict[name]:
                if abs(t-time)<=60 and p!=place:
                    invalid.add(i)
                    invalid.add(j)
                    
            
            transDict[name].add((i, time, place))
            # print(invalid)
        
        return [transactions[index] for index in invalid]
                
            
            
            
        