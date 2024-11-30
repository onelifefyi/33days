# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Approach:
# Create a new list (and a var to keep track of head)
# Have two pointers, starting with head of list1 and list2
# Compare both the values, insert the lesser one to the new list
# Move the new list to it's next
# Do this till one of the lists becomes empty
# Finally, attach the remaining list to the end of new list

# Time O(n + m) | Space O(1)

def mergeTwoLists(list1, list2):
    result = ListNode()
    start = result
    while list1 and list2:
        if list1.val <= list2.val:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
        result = result.next
    result.next = list1 if list1 else list2
    return start.next
