class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.count = 0
        self.prev = self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache[key][1]+=1
        self.time +=1
        self.cache[key][2] = self.time
        return self.cache[key][0]


    def put(self, key: int, value: int) -> None:
        if self.cap<=0:
            return
        self.time+=1
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] = self.time
            return
        if len(self.cache) >= self.cap:
            minf = float('inf')
            mint = float('inf')
            lfu = None
            for k, (_,freq,ts) in self.cache.items():
                if freq < minf or (freq==minf and ts<mint):
                    minf = freq
                    mint = ts
                    lfu = k
            if lfu is not None:
                del self.cache[lfu]
        self.cache[key] = [value, 1, self.time]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)