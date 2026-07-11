class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        res = []
        for i in range(len(nums)):
            a = nums[i]
            count[a]-=1
            if i and a==nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                b=nums[j]
                count[b]-=1
                if j-1>i and nums[j]==nums[j-1]:
                    continue
                target = -(a+b)
                if count[target]>0:
                    res.append([a,b,target])
            for j in range(i+1, len(nums)):
                count[nums[j]]+=1
        return res


