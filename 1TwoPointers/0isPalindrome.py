# https://leetcode.com/problems/valid-palindrome/description/

# Appraoch:
# Step 1: Clean the list
# Step 2: Check with reversed
# Time O(n) | Space O(n)

# Approach:
# Have two pointers, left and right
# If any char at the pointer is non-alphanumeric move the pointer closer
# if alphanueric and not equal return False
# Otherwise move the pointers closer till left <= right
# Time O(n) | Space O(1)

def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left <= right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome(s))