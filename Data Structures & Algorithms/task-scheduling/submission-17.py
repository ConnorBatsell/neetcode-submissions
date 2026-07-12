class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        freq = defaultdict(int)
        for task in tasks:
            freq[task]+=1
        heap = []
        for key,val in freq.items():
            heapq.heappush(heap, -val)
        q = deque()
        while heap or q:
            cycles+=1
            if heap:
                a = heapq.heappop(heap)
                if a+1!=0:
                    q.append([a+1,cycles+n])
            if q and q[0][1]==cycles:
                heapq.heappush(heap, q.popleft()[0])

                
        return cycles
            






            