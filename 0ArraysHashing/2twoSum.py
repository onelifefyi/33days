# https://leetcode.com/problems/two-sum/description/

# Brute Approach:
# Check all possible combination using nested loop
# Time O(n^2) | Space O(1)

# Better Appraoch:
# Create a hashmap to store the (target - num) as key and index as value
# If the num in hashmap, return current index and hashmap[num] as list
# Time O(n) | Space O(n)

def twoSum(nums, target):
    required_hashset = {}
    for index, num in enumerate(nums):
        if num in required_hashset:
            return [index, required_hashset[num]]
        required_hashset[target - num] = index
    raise Exception("Pair does not exist")

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))