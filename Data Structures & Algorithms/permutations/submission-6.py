class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            temp = []
            for p in res:
                for i in range(len(p)+1):
                    a = p.copy()
                    a.insert(i, n)
                    temp.append(a)
            res = temp
        return res

        