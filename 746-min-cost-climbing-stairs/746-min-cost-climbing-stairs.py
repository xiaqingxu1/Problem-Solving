class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost1, cost2 = cost[0], cost[1]
        # cost = 0
        
        for i in range(2, len(cost)):
            temp = min(cost1 + cost[i], cost2 + cost[i])
            cost1, cost2 = cost2, temp
        
        return min(cost1, cost2)