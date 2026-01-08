# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sub_sum.append(s)
            return s

        sub_sum = []
        total = dfs(root)

        ans = max(s * (total - s) for s in sub_sum)
        return ans % 1_000_000_007