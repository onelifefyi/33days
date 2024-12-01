# https://leetcode.com/problems/number-of-1-bits/

# Approach:
# Keep track of count, by adding the '&' operation with 1 and keep right shifting till it becomes 0
# Return count
# Time O(log2(n)) | Space O(1)

# Better approach:
# We know that for any number num, num-1 will have all the bits the same as num until before the last set bit in num
# And all the lower significance bits will be different
# So, esentially when we perform num & (num-1), we are removing the last set bit from the num
# Time O(weight) or O(1) assuming every variable represented using same number of bits | Space O(1)

def hammingWeight(n):
    count = 0
    while n:
        count += 1
        n = n & (n-1)
    return count

n = 11
print(hammingWeight(n))