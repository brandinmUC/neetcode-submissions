# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # original list
        dummy = dummy.next

        cur = dummy2 = ListNode() # k-len lists
        dummy3 = curlst = ListNode() # final result
        m = k

        while dummy:
            k -= 1
            dummy2.next = ListNode(dummy.val)
            dummy2 = dummy2.next
            dummy = dummy.next

            if k == 0:
                k = m
                curlst.next = self.reverseList(cur.next)

                while curlst.next:
                    curlst = curlst.next
                cur = dummy2 = ListNode()
            
        if m > k > 0: # Remaining node check
            curlst.next = cur.next
            cur = curlst.next

        return dummy3.next

    def reverseList(self, lst):
        prev, curr = None, lst

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
