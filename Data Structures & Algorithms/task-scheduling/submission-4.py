class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task]+=1
        heap = []
        for key,val in count.items():
            heapq.heappush(heap, -val)
        res = 0
        temp = deque()
        while heap or temp:
            res+=1
            if heap:
                a=heapq.heappop(heap)
                if a+1:
                    temp.append([a+1, res+n])
            if temp:
                if temp[0][1]==res:

                    heapq.heappush(heap,temp.popleft()[0])
        return res



            