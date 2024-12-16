# https://leetcode.com/problems/climbing-stairs/


# Approach:
# To get to any stair there are two ways, 1st from previous step and 2nd from 2 steps before
# We can keep building by finding how many ways are their to get to prev stair + the one before the prev
# Time O(n) | Space O(n)
def climbStairs(n):
    if n <= 2:
        return n
    possibleWays = [0] * n
    possibleWays[0] = 1
    possibleWays[1] = 2
    stair = 2
    while stair < n:
        possibleWays[stair] = possibleWays[stair-1] + possibleWays[stair-2]
        stair += 1
    return possibleWays[-1]

# n = 3
n = 4
print(climbStairs(n))