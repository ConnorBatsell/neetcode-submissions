class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [0]*(len(cost)+1)
        cache[0] = 0
        cache[1] = 0
        for i in range(2,len(cost)+1):
            cache[i] = min(cache[i-1]+cost[i-1], cache[i-2]+cost[i-2])
        return cache[len(cost)]

            