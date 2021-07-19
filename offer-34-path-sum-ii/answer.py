# 二叉树
注：以 Python 语言为例，记录路径时若直接执行 res.append(path) ，则是将此 path 对象加入了 res ；后续 path 改变时， res 中的 path 对象也会随之改变，因此无法实现结果记录。正确做法为： 
      Python: res.append(list(path)) ；原理是避免直接添加 path 对象，而是 拷贝 了一个 path 对象并加入到 res 。

 算法流程：
pathSum(root, sum) 函数：

初始化： 结果列表 res ，路径列表 path 。
返回值： 返回 res 即可。
recur(root, tar) 函数：

递推参数： 当前节点 root ，当前目标值 tar 。
终止条件： 若节点 root 为空，则直接返回。
递推工作：
路径更新： 将当前节点值 root.val 加入路径 path 。
目标值更新： tar = tar - root.val（即目标值 tar 从 sum 减至 00 ）。
路径记录： 当 ① root 为叶节点 且 ② 路径和等于目标值 ，则将此路径 path 加入 res 。
先序遍历： 递归左 / 右子节点。
路径恢复： 向上回溯前，需要将当前节点从路径 path 中删除，即执行 path.pop() 。

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))  # 见最上面的注解
            recur(root.left, tar)  # 先序遍历就是先判断遍历结果（终止条件），在写这两行，中序遍历就是在这两行代码中间判断终止条件，后序遍历就是在这两行代码后面判断终止条件。ps:嘿嘿我会盲打了
            recur(root.right, tar)
            path.pop()  # 如果不加（），就是只出栈最后一个数，加了（）就是清空path数组
        recur(root, sum)
        return res

