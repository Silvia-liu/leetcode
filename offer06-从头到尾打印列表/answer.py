# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#

class Solution:
    def reversePrint(self, head: List) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)  # 读取head的值
            head = head.next  # head指针向后一位
        return stack[::-1]  # list倒序排列
