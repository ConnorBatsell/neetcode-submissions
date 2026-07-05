class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x:x[0])
        av = [i for i in range(n)]
        used = []
        count = [0]*n
        for start, end in meetings:
            while used and used[0][0]<start:
                a,b = heapq.heappop(used)
                heapq.heappush(av, b)
            if not av:
                en, room = heapq.heappop(used)
                end = en + (end-start)
                heapq.heappush(av, room)
            room = heapq.heappop(av)
            heapq.heappush(used, (end, room))
            count[room]+=1
        return count.index(max(count))