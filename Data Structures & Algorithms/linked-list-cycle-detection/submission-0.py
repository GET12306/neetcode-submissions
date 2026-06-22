# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        passed = set()
        while head:
            if head not in passed:
                passed.add(head)
                head = head.next
            else:
                return True
        return False