# Approach:
# Keep storing the minimum cost it takes to reach the step
# Use the previous two step's minimum cost to calculate for any specific step
# Finally return the minimum cost (after adding the final cost to climb from the step)
# Time O(n) | Space O(n)
def minCostClimbingStairs(cost):
    minCost = [0] * len(cost)
    minCost[0] = 0
    minCost[1] = 0
    step = 2
    while step < len(cost):
        minCost[step] = min(minCost[step-1] + cost[step-1], minCost[step-2] + cost[step-2])
        step += 1
    # print(minCost)
    return min(minCost[-1] + cost[-1], minCost[-2] + cost[-2])

cost = [10,15,20]
print(minCostClimbingStairs(cost))