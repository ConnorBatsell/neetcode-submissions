class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task]+=1
        heap = []
        for key,val in count.items():
            heapq.heappush(heap, -val)
        q = deque()
        count = 0
    
        while heap or q:
            count+=1
            if heap:
                a = heapq.heappop(heap)
                if a+1:
                    q.append([a+1, count+n])
            if q and q[0][1]==count:
                    heapq.heappush(heap, q.popleft()[0])
        return count





            