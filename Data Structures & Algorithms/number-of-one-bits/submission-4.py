class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(0,32):
            t = 1<<i
            if t&n:
                count+=1
        return count