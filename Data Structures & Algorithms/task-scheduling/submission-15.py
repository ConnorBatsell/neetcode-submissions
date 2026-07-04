class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for t in tasks:
            d[t]+=1
        h = []
        for k,v in d.items():
            heapq.heappush(h, -v)
        q = deque()
        count = 0
        while h or q:
            count+=1
            if h:
                a = heapq.heappop(h)
                if a+1:
                    q.append([a+1, count+n])
            if q and q[0][1]==count:
                heapq.heappush(h,q.popleft()[0])
        return count





            