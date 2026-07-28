class TimeMap:

    def __init__(self):
        self.t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t:
            self.t[key] = []
        self.t[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        arr = self.t.get(key,[])
        l=0
        r = len(arr)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m+1
            else:
                r = m-1
        return res
        

        
