# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach:
# Recursively invert and swap the left and right subtree.
# Time O(n) | Space O(n)
# Need to double check on time/space complexity
def invertTree(root):
    if not root:
        return None
    root.right, root.left = root.left, root.right
    invertTree(root.right)
    invertTree(root.left)
    return root