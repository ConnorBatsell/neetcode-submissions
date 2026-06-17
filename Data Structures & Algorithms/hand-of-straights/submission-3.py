class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = defaultdict(int)
        for val in hand:
            freq[val]+=1
        if len(hand)%groupSize!=0:
            return False
        for val in sorted(freq):
            count = freq[val]
            if count >0:
                for i in range(val, val+groupSize):
                    if freq[i]< count:
                        return False
                    freq[i]-=count
            hand.pop(0)
        return True
