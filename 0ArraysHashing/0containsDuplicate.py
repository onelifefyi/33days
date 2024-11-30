# https://leetcode.com/problems/contains-duplicate/

# Brute Approach:
# Check all possible pairs using nested loop 
# Time: O(n^2) | Space: O(1)

# Better Approach:
# Keep storing the elements in a set
# If duplicate appears return True, else return False
# Time O(n) | Space O(n)
def containsDuplicate(nums):
    items = set()
    for num in nums:
        if num in items:
            return True
        items.add(num)
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))