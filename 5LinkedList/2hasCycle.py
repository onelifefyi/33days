# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach: Use two pointers, slow and fast.
# Slow increments at 1, fast increments at 2
# If before fast reaches the end, both the pointers are same means it has cycle
# Time O(n) | Space O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False