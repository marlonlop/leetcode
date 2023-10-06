class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # good edge case to think about if we don't know cost length
        # if len(cost) == 1: return cost[0]
        # if len(cost) == 0: return -1

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            #cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
            cost[i] += min(cost[i + 1], cost[i + 2]) # simplified

        # we can return this because we are guaranteed that len(cost) >= 2
        return min(cost[0], cost[1]) 