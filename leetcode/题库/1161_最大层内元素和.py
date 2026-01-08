# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -inf
        ans = 0

        q = [root]
        level = 1
        while q:
            tmp = q
            q = []
            s = 0
            for node in tmp:
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if s > max_sum:
                max_sum = s
                ans = level

            level += 1

        return ans