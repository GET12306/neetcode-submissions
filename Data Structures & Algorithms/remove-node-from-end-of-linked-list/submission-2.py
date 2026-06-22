# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 反转
        rev_head = self.createR(head)
        # 删除正数第 n 个节点（需要处理删除头节点）
        dummy = ListNode(0, rev_head)
        prev, curr = dummy, rev_head
        for _ in range(n-1):
            prev = curr
            curr = curr.next
        prev.next = curr.next   # 删除 curr
        # 反转回来
        new_rev_head = dummy.next
        return self.createR(new_rev_head)


    def createR(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            