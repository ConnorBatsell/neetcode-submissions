class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        down1 = down2 = 0 
        for i in range(len(cost) - 1, -1, -1):
            cur = cost[i] + min(down1, down2)
            down2 = down1
            down1 = cur
        return min(down1, down2) 