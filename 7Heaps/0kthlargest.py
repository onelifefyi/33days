# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Approach:
# We only need to keep track of top k numbers
# So, after creating the heap, keep only max k numbers
# If something smaller than kth max shows up simply discard
# Otherwise pop the min from the heap and push the new item
# Finally return the 0th element


import heapq

class KthLargest:
    
    # Time O(n) | Space O(n)
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        for i in range(len(nums) - k):
            heapq.heappop(self.heap)

    # Time O(n) | Space O(1)
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        if val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)