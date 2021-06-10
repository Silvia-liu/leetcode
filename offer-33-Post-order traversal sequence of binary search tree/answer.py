# 方法一
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True # 如果i>=j说明数组中只有一个数，其实i>j的情况不太可能发生
            p = i # 此时p为左端点
            while postorder[p] < postorder[j]: p += 1  # 如果从左边来的p小于数组中的索引j对应的值
            m = p # 把左边第一个大于根节点的数记录为m，这个m属于右子树范畴的某个节点
            while postorder[p] > postorder[j]: p += 1  
                # 执行上面这句话之前的p是（左边第一个大于根节点的数，即右子树），执行这句话就是：在一个后序遍历的小分叉中从右子树到根节点，while结束以后p就是根节点，即p == j
            return p == j and recur(i, m - 1) and recur(m, j - 1)  # recur(i, m - 1) and recur(m, j - 1)这些是递归进行判断是否为后序遍历的搜索二叉树
        return recur(0, len(postorder) - 1)

