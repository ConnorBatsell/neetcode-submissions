class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        count = 0
        for i in range(0,n+1):
            count = 0
            temp = i
            while not i==0:
                count+= i%2
                i = i//2
            out.append(count)
        return out