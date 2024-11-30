# https://leetcode.com/problems/binary-search/description/

# Brute approach:
# Just iterate throught the array, if present, return index, otherwise return -1
# Time O(n) | Space O(1)

# Binary search approach:
# Just use binary search, lol
# Details -> Take two pointers, left and right pointing at 0 and len - 1 resp
# Find mid point, if that's equal return mid
# If it's smaller than traget, move left to mid
# If it's greater than target, move right to mid
# Do this till left <= right
# Time O(logn) | Space O(1)

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


nums = [-1,0,3,5,9,12]
target = 9
# nums = [-1,0,3,5,9,12]
# target = 2
print(search(nums, target))