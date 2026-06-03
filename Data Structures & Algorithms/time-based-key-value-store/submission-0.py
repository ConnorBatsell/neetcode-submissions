class TimeMap:

    def __init__(self):
        self.t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t:
            self.t[key] = []
        self.t[key].append([value, timestamp]) 

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.t.get(key, [])
        l=0
        r = len(values)-1
        while l<=r:
            m = l+ ((r-l)//2)
            if values[m][1] <= timestamp:
                l = m+1
                res = values[m][0]
            else:
                r = m-1
        return res
