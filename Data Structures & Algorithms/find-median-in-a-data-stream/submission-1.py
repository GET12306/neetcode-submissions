class MedianFinder:

    def __init__(self):
        self.num = []

    def addNum(self, num: int) -> None:
        self.num.append(num)
        self.num.sort()

    def findMedian(self) -> float:
        if len(self.num) % 2 == 0:
            m2 = int(len(self.num)/2)
            m1 = m2 - 1
            return (self.num[m2] + self.num[m1])/2
        else:
            m = len(self.num) // 2
            return self.num[m]
        