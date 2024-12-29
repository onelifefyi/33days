# https://leetcode.com/problems/group-anagrams/

# Brute Approach:
# For each of the words, try to find the anagram and group them together in a list

# Approach:
# For each word, store them as a list inside a dict based on character frequency
# Finally return the dict converted to array

# Time O(n * m) | Where m is the size of the longest word
# Space O(n)
def groupAnagram(strs):
    result = {}
    for word in strs:
        bitArray = [0] * 26
        for ch in word:
            bitArray[ord(ch) - ord('a')] += 1
        bitTouple = tuple(bitArray)
        if bitTouple in result:
            result[bitTouple].append(word)
        else:
            result[bitTouple] = [word]
    return list(result.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))