class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for tsk in tasks:
            d[tsk]+=1
        h = []
        for key,val in d.items():
            heapq.heappush(h, [-val, key])
        time = 0
        while h:
            temp = []
            count = 0
            for _ in range(n+1):
                if h:
                    count+=1
                    cnt,key = heapq.heappop(h)
                    if cnt+1<0:
                        temp.append([cnt+1,key])
            for item in temp:
                heapq.heappush(h,item)
            if h:
                time+=n+1
            else:
                time+=count
        return time





            