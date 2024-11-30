# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
# We will need couple of variables to keep track
# Have a var next = None to keep track of next node
# Have a var curr = Head to keep track of current node
# Have a var prev = curr to keep track of previous node
# Till curr becomes None, repeat
# Set next to curr.next (store next element)
# Set curr.next to prev (point currrents next to previous element)
# Set prev to current
# Set curr to next
# Finally return prev (since curr will be None)

# Too much info, when solving keep your mind cool, think about what things do we need to keep track of

# Time O(n) | Space O(1)

def reverseList(head):
    prev = None
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
