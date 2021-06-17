class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return  # 如果root为空，则说明root的上一节没有子节点
            dfs(root.right)  # 如果有子节点，先进入右边，即中序遍历的逆序
            if self.k == 0: return  # 先从右边找，如果右边就满足条件：有第K大节点，那就return
            self.k -= 1  # 减一，说明离第k大子节点更进一步了。
            if self.k == 0: self.res = root.val   # self.k == 0时，说明这时的root就是第k大子节点了，返回self.res
            dfs(root.left)  # 如果右子树没找到，那就找左子树
            #

        self.k = k
        dfs(root)
        return self.res
    
    
# 本文解法基于性质：二叉搜索树的中序遍历为递增序列。根据此性质，易得二叉搜索树的 中序遍历倒序 为 递减序列 。因此，求 “二叉搜索树第 k 大的节点” 可转化为求 “此树的中序遍历倒序的第 k 个节点
