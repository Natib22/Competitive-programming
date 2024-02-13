# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        myarray=[]
        current= head
        while current:
            myarray.append(current.val)
            current= current.next
        i,j= 0, len(myarray)-1
 
        while i< j :
            if myarray[i] != myarray[j]:
                return False
            i+=1
            j-=1
        return True
         
        