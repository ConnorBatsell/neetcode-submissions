class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            t = []
            for p in res:
                for i in range(len(p)+1):
                    a = p.copy()
                    a.insert(i, n)
                    t.append(a)
            res = t
        return res

        