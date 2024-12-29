# https://leetcode.com/problems/top-k-frequent-elements/

# Appraoch:
# Create an array of list of size n
# Using nested loop, get the freq of each number and fill it in the array created above
# Finally return the last k elements from that array
# Time O(n^2) | Space O(n)

# Better approach:
# Use hash map to get the frequency of each items
# Then, fill the resultArray using that hash map
# Finally return the last k elements from that array
# Time O(n) | Space O(n)

def topKFrequent(nums, k):
    freqTable = {}
    for num in nums:
        if num in freqTable: freqTable[num] += 1
        else: freqTable[num] = 1

    # Note that [[]] * something, won't work because it uses the same reference of the list
    freqArr = [[] for _ in range(len(nums) + 1)]

    for num in freqTable:
        freqArr[freqTable[num]] += [num]

    result = []
    size = k
    for nums in freqArr[::-1]:
        while nums and k:
            result.append(nums.pop())
            k -= 1
        if k == 0:
            return result
        

# nums = [1,1,1,2,2,3]
# k = 2
nums = [1]
k = 1
print(topKFrequent(nums, k))