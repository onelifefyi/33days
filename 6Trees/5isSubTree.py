# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # Time O(n) | Space O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # Time O(n*m) (worst case, all tree node having same value as that of subRoot)
    # Space O(n)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSame = False
        stack = []
        if root: stack.append(root)
        while stack:
            curr = stack.pop()
            if curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot): return True
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
        return False