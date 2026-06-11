class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            if task not in count:
                count[task]=1
            else:
                count[task]+=1
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time =0
        q = deque()
        while maxHeap or q:
            time+=1
            if maxHeap:
                a=heapq.heappop(maxHeap)
                if a+1:
                    q.append([a+1, time+n])
            if q:
                if q[0][1]==time:
                    b = q.popleft()
                    heapq.heappush(maxHeap, b[0])
        return time
            