# 方法一，和前两题一样，只是多个判断奇偶层数
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0: tmp.append(node.val) # 奇数层 -> 插入队列尾部   这里注意，是判断res（结果）里面的层数已经有几层了。
                else: tmp.appendleft(node.val) # 偶数层 -> 插入队列头部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res
# 方法二  分左右子树的
# 层序遍历 + 双端队列（奇偶层逻辑分离）
# 方法一代码简短、容易实现；但需要判断每个节点的所在层奇偶性，即冗余了 N 次判断。
# 通过将奇偶层逻辑拆分，可以消除冗余的判断。
# 算法流程：
# 与方法一对比，仅 BFS 循环不同。

# BFS 循环： 循环打印奇 / 偶数层，当 deque 为空时跳出；
# 打印奇数层： 从左向右 打印，先左后右 加入下层节点；
# 若 deque 为空，说明向下无偶数层，则跳出；
# 打印偶数层： 从右向左 打印，先右后左 加入下层节点；

