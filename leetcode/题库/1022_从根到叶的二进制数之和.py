class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 从根到 node（不含）的路径值为 num
        def dfs(node: Optional[TreeNode], num: int) -> None:
            nonlocal ans
            if node is None:
                return
            num = num << 1 | node.val
            if node.left is None and node.right is None:
                ans += num
                return
            dfs(node.left, num)
            dfs(node.right, num)

        ans = 0
        dfs(root, 0)
        return ans