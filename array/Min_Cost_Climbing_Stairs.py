#problem link https://leetcode.com/problems/min-cost-climbing-stairs/
#Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(0,len(cost) -2):
            cost[i+2] += min(cost[i], cost[i+1])
        return min(cost[-2], cost[-1])