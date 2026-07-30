class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            cache[i] = max(cache[i-1], nums[i]+cache[i-2])
        m1 = cache[len(nums)-2]
        cache = [-1]*len(nums)
        cache[1] = nums[1]
        cache[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            cache[i] = max(cache[i-1], nums[i]+cache[i-2])
        m2 = cache[len(nums)-1]
        return max(m1,m2)


        
            
        