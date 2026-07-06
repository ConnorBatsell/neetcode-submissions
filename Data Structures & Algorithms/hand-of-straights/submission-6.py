class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        f = defaultdict(int)
        for n in hand:
            f[n]+=1
        for i in sorted(hand):
            count = f[i]
            if count>0:
                for j in range(i, i+groupSize):
                    if f[j]<count:
                        return False
                    f[j]-=count
        return True


