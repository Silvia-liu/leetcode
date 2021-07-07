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
