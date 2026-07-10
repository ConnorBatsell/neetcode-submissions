class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        for i in range(len(nums)):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        slowTwo = 0
        while slowTwo!=slow:
            slowTwo=nums[slowTwo]
            slow = nums[slow]
        return slow
        