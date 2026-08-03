class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x:x[0])
        available = [i for i in range(n)]
        used = []
        count = [0]*n
        for start,end in meetings:
            while used and used[0][0]<=start:
                x,y = heapq.heappop(used)
                heapq.heappush(available, y)
            if not available:
                x,y = heapq.heappop(used)
                heapq.heappush(available, y)
                end = x + (end-start)
            x = heapq.heappop(available)
            heapq.heappush(used, (end, x))
            count[x]+=1
        return count.index(max(count))
