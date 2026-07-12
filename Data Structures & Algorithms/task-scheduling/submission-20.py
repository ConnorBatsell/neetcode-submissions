class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        counts = defaultdict(int)
        for task in tasks:
            counts[task]+=1
        h = []
        for key,val in counts.items():
            heapq.heappush(h, -val)
        q = deque()
        while h or q:
            cycles+=1
            if h:
                x = heapq.heappop(h)
                if x+1:
                    q.append([x+1, cycles+n])
            if q and q[0][1]==cycles:
                heapq.heappush(h, q.popleft()[0])
        return cycles

            






            