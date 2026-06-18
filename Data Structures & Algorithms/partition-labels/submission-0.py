class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexC = defaultdict(int)
        for i,c in enumerate(s):
            indexC[c] = i
        out = []
        end = 0
        size = 0
        for i,c in enumerate(s):
            size+=1
            end = max(end,indexC[c])

            if i==end:
                out.append(size)
                size = 0
        return out
