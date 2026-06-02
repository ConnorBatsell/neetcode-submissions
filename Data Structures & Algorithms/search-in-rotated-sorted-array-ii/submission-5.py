class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        res = nums[0]
        while l<=r:
            m = l + ((r-l)//2)
            if nums[m]==target:
                return True
            elif nums[m]==nums[l]:
                l+=1
            elif nums[m] >= nums[l]:
                if target>= nums[l] and target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if target>nums[m] and target<=nums[r]:
                    l = m+1
                else:
                    r=m-1
        return False