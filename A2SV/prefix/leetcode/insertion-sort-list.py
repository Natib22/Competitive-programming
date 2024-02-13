# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(-6000, head)


        current = head.next
        prev = head
        while current:
            if current.val < prev.val:
                ins = dummy.next
                tracker = dummy
                
                while current.val > ins.val:
                    ins= ins.next
                    tracker = tracker.next

                prev.next = current.next
                current.next = ins
                tracker.next = current
                current= prev.next
            else:
                prev = prev.next
                current = current.next
                
        return dummy.next



                

        