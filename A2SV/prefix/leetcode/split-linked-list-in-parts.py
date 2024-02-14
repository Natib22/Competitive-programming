# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None] * k

        size = 0
        current = head
        myarray = []
        while current:
            size += 1
            current = current.next
        rem = size % k

        current = head
        for _ in range(k):
            part_size = size // k
            if rem > 0:
                part_size += 1
                rem -= 1

            if part_size == 0:
                myarray.append(None)
            else:
                myarray.append(current)
                for _ in range(part_size - 1):
                    current = current.next
                current.next, current = None, current.next

        return myarray
        