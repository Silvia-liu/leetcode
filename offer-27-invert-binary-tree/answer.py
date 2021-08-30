# 二叉树问题again
#多看多写
#写完了写完了终于写完了







# 方法一 辅助栈法
class Solition:
    def minrrorTree(self,root:TreeNode) -> TreeNode:
        if not root:return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left,node.right=node.right,node.left
        return root
    
# dfs辅助栈
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def dfs(tree):
            if tree.right or tree.left:
                tree.right,tree.left = tree.left,tree.right
            if tree.left:
                dfs(tree.left)
            if tree.right:
                dfs(tree.right)
        if not root:
            return 
        dfs(root)
        # print(root)
        return root
# 递归
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root

