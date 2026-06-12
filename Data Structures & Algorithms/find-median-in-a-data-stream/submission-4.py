class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h1, -num)
        a = heapq.heappop(self.h1)
        heapq.heappush(self.h2, -a)
        if len(self.h2) > len(self.h1):
            b = heapq.heappop(self.h2)
            heapq.heappush(self.h1, -b)


    def findMedian(self) -> float:
        if (len(self.h1) + len(self.h2))%2==0:
            return (-self.h1[0] + self.h2[0])/2
        else:
            return -self.h1[0]
        
            