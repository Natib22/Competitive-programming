# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        oddhead = head
        evenhead= head.next
        dummy = evenhead
        while oddhead.next and evenhead.next:
            oddhead.next = evenhead.next
            oddhead = oddhead.next
            evenhead.next = oddhead.next
            evenhead = evenhead.next
            
        oddhead.next = dummy
        return head

       
        


        
                
                


        