# https://leetcode.com/problems/reverse-bits/

# Brute Approach:
# Keep performing '&' operation with 1, and '|' operation with result then right shift
# Time O(1) | Space O(1)

def reverseBits(n):
    result = 0
    for i in range(32):
        bit = n & 1
        result = result << 1
        result = result | bit
        n = n >> 1
    return result

n = 43261596
print(reverseBits(n))