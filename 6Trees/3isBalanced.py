# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First principle, based on the max height of the tree and number of element, we can find if it's balanced or not. We can find max possible length of balanced tree based on number of elements. We compare that with max depth.
# Another first principle, if at any point, if the max depth of left and right subtree differ by more than one, it's not balanced.
# Approach: DFS
# Time O(n) | Space O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))
        if not root: return True
        is_balanced = abs(dfs(root.left) - dfs(root.right)) <= 1
        if not is_balanced:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)