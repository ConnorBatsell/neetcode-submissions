class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        maxSum = r
        while l<=r:
            m = l + ((r-l)//2)
            runningCount = 0
            numSplits = 0
            for num in nums:
                runningCount += num
                if runningCount > m:
                    numSplits+=1
                    runningCount = num
            if numSplits <= k-1:
                maxSum = min(maxSum, m)
                r=m-1
            else:
                l=m+1
        return maxSum