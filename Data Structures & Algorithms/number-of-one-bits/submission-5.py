class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for i in range(32):
            t = 1<<i
            if t&n:
                c+=1
        return c