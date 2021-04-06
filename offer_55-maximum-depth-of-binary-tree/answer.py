class Solution:
    # # 深度优先遍历dfs--后序遍历
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root:return 0
    #     return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    # 广度优先遍历bfs--层序遍历
    def maxDepth(self,root:TreeNode)->int:
        if not root: return 0
        queue,res = [root], 0        
        while queue:
            tmp = []
            for node in queue:
                if node.left:tmp.append(node.left)
                if node.right:tmp.append(node.right)
            res += 1
            queue = tmp
        return res
