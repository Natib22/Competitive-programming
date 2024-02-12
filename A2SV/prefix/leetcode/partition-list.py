# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less= ListNode()
        more= ListNode()
        res=less
        dummy = more
        current =head
        while current:
            if current.val < x:
                less.next = current
                current = current.next
                less= less .next
                less.next =None
            else:
                more.next = current
                current = current.next
                more= more.next
                more.next =None
                
            
        less.next = dummy .next
        return res.next
        