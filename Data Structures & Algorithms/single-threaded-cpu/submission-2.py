class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        out = []
        heap = []
        for i in range(len(tasks)):
            heapq.heappush(heap, [tasks[i][0], tasks[i][1], i])
        available = []
        time = 0
        while heap or available:
            while heap and heap[0][0]<=time:
                a,b,c = heapq.heappop(heap)
                heapq.heappush(available, [b,c])
            if not available:
                time = heap[0][0]
                continue
            a,b = heapq.heappop(available)
            out.append(b)
            time+=a
        return out
            


