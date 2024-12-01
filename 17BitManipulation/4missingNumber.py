# https://leetcode.com/problems/missing-number/

# Approach: 
# Bitwise XOR
# Time O(n) | Space O(1)
# def missingNumber(nums):
#         result = 0
#         for i in range(len(nums) + 1):
#             result = result ^ i
#         for num in nums:
#             result = result ^ num
#         return result

# Approach:
# Math -> Add and substract things together
# Time O(n) | Space (1)

def missingNumber(nums):
    result = 0
    for i in range(len(nums)):
        result = result + i - nums[i]
    result = result + len(nums)
    return result


nums = [3,0,1]
print(missingNumber(nums))