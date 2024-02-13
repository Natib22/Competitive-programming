# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self .check = False

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        counter = {"a":0,"b":0}
        top, bottom = headA, headB
        while headA or headB:
            if headA == headB:
                return headA
            if not headA:
                while headB:
                    headB = headB.next
                    counter["b"] += 1
                break
            if not headB:
                while headA:
                    headA = headA.next
                    counter["a"] += 1
                break
            headA = headA.next
            headB = headB.next
                
        while counter["b"]:
            bottom = bottom.next
            counter["b"] -= 1
        while counter["a"]:
            top = top.next
            counter["a"] -= 1
        
        while top:
            if top == bottom:
                return top
            top = top.next
            bottom = bottom.next
        return None
        

        