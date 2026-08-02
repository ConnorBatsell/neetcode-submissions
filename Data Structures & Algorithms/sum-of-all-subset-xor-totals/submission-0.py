class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        sub = []
        def dfs(i):
            if i==len(nums):
                temp = 0
                for num in sub:
                    temp ^= num
                self.res += temp
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return self.res