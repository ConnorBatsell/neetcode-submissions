class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        h = []
        for i in range(len(tasks)):
            heapq.heappush(h, [tasks[i][0], tasks[i][1], i])
        time = 0
        available = []
        res = []
        while h or available:
            while h and h[0][0]<=time:
                x = heapq.heappop(h)
                heapq.heappush(available, [x[1], x[2]])
            if not available:
                time = h[0][0]
                continue
            y = heapq.heappop(available)
            time += y[0]
            res.append(y[1])
        return res

            


