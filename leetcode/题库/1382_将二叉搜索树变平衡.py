from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 94. 二叉树的中序遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)        # 左
            ans.append(node.val)  # 根（这行代码移到前面就是前序，移到后面就是后序）
            dfs(node.right)       # 右

        ans = []
        dfs(root)
        return ans

    # 108. 将有序数组转换为二叉搜索树
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m = len(nums) // 2
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m + 1:])
        return TreeNode(nums[m], left, right)

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = self.inorderTraversal(root)
        return self.sortedArrayToBST(nums)
