# https://leetcode.com/problems/plus-one/description/

# Approach:
# Start from the least significant bit (rightmost item)
# Add one to it
# If it is less than 9, return the array after adding one to that item
# If it is greater than 9, set that item to 0 and maintain carry variable and 
# repeat till most significant is reached
# If carry exists, insert 1 at the start of the array and return it
# Time O(n) | Space O(1)
def plusOne(digits):
    pointer = len(digits) - 1
    carry = 1
    while pointer >= 0:
        if digits[pointer] < 9: 
            digits[pointer] += 1
            return digits
        digits[pointer] = 0
        pointer -= 1
    digits.insert(0, 1)
    return digits
        

# digits = [1,2,3]
# digits = [4,3,2,1]
digits = [9]
print(plusOne(digits))