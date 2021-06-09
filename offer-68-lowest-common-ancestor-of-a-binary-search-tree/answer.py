# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一 迭代
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val < p.val and root.val < q.val: # p,q 都在 root 的右子树中
                root = root.right # 遍历至右子节点
            elif root.val > p.val and root.val > q.val: # p,q 都在 root 的左子树中
                root = root.left # 遍历至左子节点
            else: break
        return root
    
    
# 代码优化：若可保证 p.val < q.valp.val<q.val ，则在循环中可减少判断条件，提升计算效率。
 class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p # 保证 p.val < q.val
        while root:
            if root.val < p.val: # p,q 都在 root 的右子树中
                root = root.right # 遍历至右子节点
            elif root.val > q.val: # p,q 都在 root 的左子树中
                root = root.left # 遍历至左子节点
            else: break
        return root

    
    # 首先要定位给出的两个子节点在哪，
    # 根据以上定义，若 rootroot 是 p,qp,q 的 最近公共祖先 ，则只可能为以下三种情况之一：

    # p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
    # p = root 且 q 在 root 的左或右子树中；
    # q = root 且 p 在 root 的左或右子树中；

    # ① 树为 二叉搜索树 ，② 树的所有节点的值都是 唯一 的。根据以上条件，可方便地判断 p,q 与 root 的子树关系，即：

    # 若 root.val < p.val ，则 p 在 root 右子树 中；
    # 若 root.val > p.val ，则 p 在 root 左子树 中；
    # 若 root.val = p.val ，则 p 和 root 指向 同一节点 ；
   
# 方法二 递归
# 递推工作：
# 当 p, qp,q 都在 rootroot 的 右子树 中，则开启递归 root.rightroot.right 并返回；
# 否则，当 p, qp,q 都在 rootroot 的 左子树 中，则开启递归 root.leftroot.left 并返回；
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)  # 所谓递归，就是这句话，返回将要进行的下一步计算的root.right，和上面那种解法的while循环（root = root.right）很像，
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root







