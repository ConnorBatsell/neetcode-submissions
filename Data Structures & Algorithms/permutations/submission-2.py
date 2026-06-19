class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        for n in nums:
            newP = []
            for p in perms:
                for i in range(len(p)+1):
                    a = p.copy()
                    a.insert(i, n)
                    newP.append(a)
            perms = newP
        return perms