class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        f = defaultdict(int)
        for n in hand:
            f[n]+=1
        minH = list(f.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first+groupSize):
                if i not in f:
                    return False
                f[i]-=1
                if f[i]==0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

