class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x:x[0])
        a = [i for i in range(n)]
        used = []
        count = [0 for i in range(n)]
        for s,e in meetings:
            while used and used[0][0]<s:
                x,y = heapq.heappop(used)
                heapq.heappush(a,y)
            if not a:
                x,y = heapq.heappop(used)
                heapq.heappush(a,y)
                e = x + (e-s)
            x = heapq.heappop(a)
            heapq.heappush(used, (e,x))
            count[x]+=1
        return count.index(max(count))


