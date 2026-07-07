class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        for i in range(len(s)):
            lastIndex[s[i]] = i
        res = []
        currMax = 0
        size = 0
        for i in range(len(s)):
            currMax = max(currMax, lastIndex[s[i]])
            size+=1
            if currMax==i:
                res.append(size)
                size=0
                currMax = 0
        return res
