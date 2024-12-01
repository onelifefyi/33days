# https://leetcode.com/problems/counting-bits/

# Kind of Brute Approach:
# Find the hamming weight for each number
# Time O(n) | Space O(n)

def hammingWeight(n):
    count = 0
    while n:
        count += 1
        n = n & (n-1)
    return count

def countBits(n):
    result = [hammingWeight(num) for num in range(n + 1)]
    return result

n = 5
print(countBits(n))