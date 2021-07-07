题目要求的二叉树的 从上至下 打印（即按层打印），又称为二叉树的 广度优先搜索（BFS）。BFS 通常借助 队列 的先入先出特性来实现。
算法流程：
特例处理： 当树的根节点为空，则直接返回空列表 [] ；
初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] ；
BFS 循环： 当队列 queue 为空时跳出；
      出队： 队首元素出队，记为 node；
      打印： 将 node.val 添加至列表 tmp 尾部；
      添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue ；
返回值： 返回打印结果列表 res 即可。


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []  # 空值判断
        res, queue = [], collections.deque()  # 初始化，用了python的collections.deque()，deque是双边队列，具有队列和栈的性质。相当于可以在两端操作的list
        queue.append(root)  # 初始化queue
        while queue:
            node = queue.popleft()  # 队首元素出队
            res.append(node.val)
            if node.left: queue.append(node.left)  # 这一点很重要，往queue里面追加值，追加在node.right后面，，，queue = [root, root.left, root.right, root.left.left, root.left.right]
            if node.right: queue.append(node.right)  # 上面这行注释，如果不懂，带入数组，顺着程序走一遍就通了
        return res
