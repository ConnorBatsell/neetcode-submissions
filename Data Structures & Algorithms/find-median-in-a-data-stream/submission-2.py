class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n = len(self.arr)-1
        if (n+1)%2==0:
            print(self.arr)
            return (self.arr[n//2] + self.arr[(n//2)+1])/2
        else:
            print(self.arr)
            return self.arr[n//2]
        