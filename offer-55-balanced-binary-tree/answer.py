class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
      
# 定义树节点.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
 # 带有完整测试用例
if __name__ == '__main__':
    # 方法1生成二叉树的测试用例 全部手动配置左右结点，比较繁琐
    nodelist = [TreeNode(i) for i in [4, 2, 7, 1, 3, 5, 8]]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]
    nodelist[2].right = nodelist[6]
    root = nodelist[0]
    Solution = Solution()
    Solution.maxDepth(root)
    print('Solution=', Solution.maxDepth(root))
