# https://leetcode.com/problems/valid-anagram/

# Brute Approach:
# Sort both the string and check if same
# Time O(nlogn + mlogm) | Space O(n + m)

# Better Approach:
# Create an array of size 26 (each alphabet)
# Go through s and fill the frequency in that array
# Go through t, removing the freq from the array, if it becomes -ve, return False
# Go through the array, if the value is anything other than 0, return False
# Return True
# Time O(n + m) | Space O(1)

def isAnagram(s, t):
    freq_arr = [0] * 26
    for ch in s:
        freq_arr[ord(ch) - ord('a')] += 1
    for ch in t:
        freq_arr[ord(ch) - ord('a')] -= 1
        if freq_arr[ord(ch) - ord('a')] < 0:
            return False

    for cnt in freq_arr:
        if cnt != 0:
            return False

    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))