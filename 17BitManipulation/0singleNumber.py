# https://leetcode.com/problems/single-number/description/

# Brute Approach:
# Check each possible number using nested loop
# Time O(n^2) | Space O(1)

# We know that in XOR operation, 1 is returned only if both the bits are different
# So, for two numbers if all the bits are same, it will result in 0
# If we keep performing XOR operation among all the elements of a given list
# All the duplicates will turn to 0 and only one number will remain (non-duplicate)
# Time O(n) | Space O(1)

def singleNumber(nums):
        result = 0
        for num in nums:
            result = result ^ num
        return result

nums = [4,1,2,1,2]
print(singleNumber(nums))