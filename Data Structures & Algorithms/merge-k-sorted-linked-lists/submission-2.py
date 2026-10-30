# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            res = ListNode()
            return res.next

        while len(lists) > 1:
            mergedList = []
       
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeTwoLists(l1, l2))
            
            lists = mergedList  

        return lists[0]


    def mergeTwoLists(self, lst1, lst2):
        res = dummy = ListNode()
        while lst1 and lst2:
            if lst1.val < lst2.val:
                dummy.next = lst1
                lst1 = lst1.next
            else:
                dummy.next = lst2
                lst2 = lst2.next
            dummy = dummy.next
        dummy.next = lst1 or lst2 
        return res.next
