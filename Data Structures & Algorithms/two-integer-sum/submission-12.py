class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dic:
                return [dic[a], i]
            dic[nums[i]] = i
        
        
        
