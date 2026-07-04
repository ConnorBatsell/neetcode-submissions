class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        h = []
        for i in range(len(tasks)):
            heapq.heappush(h, [tasks[i][0], tasks[i][1], i])
        res = []
        available = []
        time = 0
        while h or available:
            while h and h[0][0] <= time:
                a = heapq.heappop(h)
                heapq.heappush(available, [a[1], a[2]])
            if not available:
                time = h[0][0]
                continue
            b = heapq.heappop(available)
            time += b[0]
            res.append(b[1])
        return res

            


