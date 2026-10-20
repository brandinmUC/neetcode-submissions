# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = cpy = ListNode()
        cpy2 = head
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = cpy2
        l2 = self.reverse(slow)

        while l1 != slow and l2:
            cpy.next = l1
            l1 = l1.next
            cpy = cpy.next
            # print(cpy.val)
            cpy.next = l2
            l2 = l2.next
            cpy = cpy.next
            # print(cpy.val)
        head = dummy.next


    def reverse(self, lst):
        prev, curr = None, lst

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
