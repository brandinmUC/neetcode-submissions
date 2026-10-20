# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = dummy = ListNode()
        cpy = head

        lstlen = 0

        while head:
            lstlen += 1
            head = head.next

        target = lstlen - n
        print(lstlen, target)
        ctr = 0
        while ctr != target:
            dummy.next = cpy
            dummy = dummy.next
            cpy = cpy.next
            ctr += 1
            
        if cpy.next:
            dummy.next = cpy.next
        else:
            dummy.next = None

        return res.next

