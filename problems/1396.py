from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.userDict = {}
        # defaultdict 的高阶用法
        self.undergorundDict = defaultdict(lambda : [0, 0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.userDict[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # 这里可以用pop 效率会高一点
        startStation, startTime = self.userDict.pop(id)
        timeInterval = t - startTime
        key = (startStation,stationName)
        self.undergorundDict[key][0] += timeInterval
        self.undergorundDict[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation,endStation)
        return self.undergorundDict[key][0] / self.undergorundDict[key][1]