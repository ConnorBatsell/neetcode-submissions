class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for tsk in tasks:
            d[tsk]+=1
        h = []
        for key,val in d.items():
            heapq.heappush(h, -val)
        count = 0
        q = deque()
        while h or q:
            count+=1
            if h:
                a = heapq.heappop(h)
                if a+1:
                    q.append([a+1,n+count])
            if q and q[0][1]==count:
                heapq.heappush(h, q.popleft()[0])
            
        return count





            