# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res =  ListNode()
        current = res
        first= list1
        second = list2
        while first and second:
            if first.val > second.val:
                res.next = ListNode(second.val)
               
                second= second.next
            else:
                res.next = ListNode(first.val)
                first = first. next
            res= res.next

        if first:
            res.next=first
        else:
            res.next = second

        

        return current.next

        