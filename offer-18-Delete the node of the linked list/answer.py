# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 本题删除值为 val 的节点分需为两步：定位节点、修改引用
        # 如果待删除节点为头节点，直接返回cur.next
        if head.val == val: return head.next
        # 初始化
        pre, cur = head, head.next
        # cur不为空且不是待删除节点，则进行下一个节点的判断
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        # 经过上面两条语句，cur为待删除节点，判断cur是否为空，不为空，就更改指针指向
        if cur: pre.next = cur.next
        # 返回头节点
        return head

