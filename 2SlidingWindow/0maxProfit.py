# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Brute approach:
# Try all possible combinations (moving forward) using nested loops 
# Time O(n^2) | Space O(1)

# Approach Pointers:
# Keep track of minimum buying price
# Keep track of maxProfit that can be made
# If currentProfit > maxProfit, update the maxProfit and minimum buying price
# Time O(n) | Space O(1)

# Approach Sliding Window:
# Have a window of left, right at index 0, 1 resp
# Left always points to the lowest price
# We keep track of max profit throughout the process
# Time O(n) | Space O(1)

def maxProfit(prices):
    maxProfit = 0
    left, right = 0, 1
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1
    return maxProfit

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
print(maxProfit(prices))