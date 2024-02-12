# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left,right= ListNode(),ListNode()
        left.next,right.next= head,head
        ans = left
        for i in range(n):
            right= right.next
        while right.next:
            left= left.next
            right= right.next
        
        left.next= left.next.next
  
        return ans.next
        

        
        