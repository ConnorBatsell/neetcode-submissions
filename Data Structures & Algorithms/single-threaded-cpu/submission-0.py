class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        out = []
        heap = []
        time = 0
        for i in range(len(tasks)):
            heapq.heappush(heap, (tasks[i], i))
        available = []
        while heap or available:
            while heap and heap[0][0][0] <= time:
                (enqueueTime, processTime), i = heapq.heappop(heap)
                heapq.heappush(available, (processTime, i))
            if not available:
                time = heap[0][0][0]
                continue
            processTime, i = heapq.heappop(available)
            time+=processTime
            out.append(i)
            
        return out

