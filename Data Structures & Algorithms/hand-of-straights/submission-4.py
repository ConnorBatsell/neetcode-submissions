class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = defaultdict(int)
        for val in hand:
            freq[val]+=1
        if len(hand)%groupSize!=0:
            return False
        for val in sorted(freq):
            c = freq[val]
            if c>0:
                for i in range(val, val+groupSize):
                    if freq[i]<c:
                        return False
                    freq[i]-=c
        return True

