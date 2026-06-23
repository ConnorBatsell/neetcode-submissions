class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        count = 0
        for i in range(0,n+1):
            count = 0
            for j in range(0, 32):
                bitmask = 1<<j
                if i&bitmask:
                    count+=1
            out.append(count)
        return out