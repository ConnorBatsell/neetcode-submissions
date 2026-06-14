class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        out = []
        heap = []
        time = 0
        count = 0
        for task in tasks:
            heapq.heappush(heap, [task[0], task[1], count])
            count+=1
        available = []
        while heap or available:
            while heap and heap[0][0]<=time:
                a,b,c = heapq.heappop(heap)
                heapq.heappush(available, (b,c))
            if not available:
                time = heap[0][0]
                continue
            proc, i = heapq.heappop(available)
            time+=proc
            out.append(i)
        
        return out

