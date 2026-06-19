class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                       # canonical order so dups collapse
        seen = set()                      # real set, not {}
        sub = []
        def dfs(i):
            if i >= len(nums):
                seen.add(tuple(sub))      # tuple: hashable + snapshot
                return
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)
        dfs(0)
        return [list(t) for t in seen]    # tuples back to lists for output