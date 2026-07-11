class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(numbers)):
            ans = target-numbers[i]
            if ans in cache:
                return [cache[ans]+1, i+1]
            cache[numbers[i]] = i