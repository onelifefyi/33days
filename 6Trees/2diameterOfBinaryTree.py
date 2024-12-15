# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: DFS
# The diameter at any point is going to be the sum of max length at left and max length at right subtree
# We keep track of diameter at every single node (max of it in res)
# Finally return the result
# Time O(n) | Space O(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            self.res = max(self.res, left_height + right_height)
            return 1 + max(left_height, right_height)
        dfs(root)
        return self.res