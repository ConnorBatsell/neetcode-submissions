class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(tasks)):
            heapq.heappush(heap, [tasks[i][0], tasks[i][1], i])
        res = []
        available = []
        time = 0
        while heap or available:
            while heap and heap[0][0]<=time:
                a = heapq.heappop(heap)
                heapq.heappush(available, [a[1], a[2]])
            if not available:
                time = heap[0][0]
                continue
            b = heapq.heappop(available)
            time+=b[0]
            res.append(b[1])
        return res

            


