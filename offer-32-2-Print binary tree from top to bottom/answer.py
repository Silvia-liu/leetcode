题目要求的二叉树的 从上至下 打印（即按层打印），又称为二叉树的 广度优先搜索（BFS）。BFS 通常借助 队列 的先入先出特性来实现。
算法流程：
特例处理： 当树的根节点为空，则直接返回空列表 [] ；
初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] ；
BFS 循环： 当队列 queue 为空时跳出；
      出队： 队首元素出队，记为 node；
      打印： 将 node.val 添加至列表 tmp 尾部；
      添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue ；
返回值： 返回打印结果列表 res 即可。

注：题目新要求，从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。如下
[
  [3],
  [9,20],
  [15,7]
]
 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []  # 空值判断
        res, queue = [], collections.deque()  # 初始化，用了python的collections.deque()，deque是双边队列，具有队列和栈的性质。相当于可以在两端操作的list
        queue.append(root)  # 初始化queue
        while queue:
            temp = []  # 看似简单，就是在当前层里循环并把temp  append加进res，但是，我就是没想出来。。。。。多做题吧
            for _ in range(len(queue)):
                node = queue.popleft()  # 队首元素出队
                temp.append(node.val)
                if node.left: queue.append(node.left)  # 这一点很重要，往queue里面追加值，追加在node.right后面，，，queue = [root, root.left, root.right, root.left.left, root.left.right]
                if node.right: queue.append(node.right)  # 上面这行注释，如果不懂，带入数组，顺着程序走一遍就通了
            res.append(temp)
        return res
