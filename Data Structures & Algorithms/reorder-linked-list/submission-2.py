# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = self.reverseList(slow.next)
        slow.next = None
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2

    def reverseList(self, lst):
        prev = None

        while lst:
            tmp = lst.next
            lst.next = prev
            prev = lst
            lst = tmp

        return prev
