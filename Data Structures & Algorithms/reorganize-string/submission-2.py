class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c]+=1
        h = []
        for key,val in d.items():
            heapq.heappush(h, (-val, key))
        hold = None
        out = ""
        while h:
            count,c = heapq.heappop(h)
            out += c
            count+=1
            if hold:
                heapq.heappush(h, hold)
                hold = None
            if count!=0:
                hold = (count,c)
        return out if len(out)==len(s) else ""






        