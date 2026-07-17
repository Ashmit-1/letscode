# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from functools import lru_cache
        @lru_cache()
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)
        res = 0
        def dia(root):
            nonlocal res
            if not root:
                return 
            res = max(res, height(root.left) + height(root.right))
            dia(root.left)
            dia(root.right)
        dia(root)
        return res
        