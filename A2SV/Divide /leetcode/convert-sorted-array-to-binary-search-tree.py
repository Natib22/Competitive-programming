# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        def my(arr):
            if len(arr) == 1:
                node = TreeNode(arr[0])
                node.left = None
                node.right = None
                return node
            elif not arr:
                return None
            mid= len(arr)//2
        
            curr = TreeNode(arr[mid])

            curr.left  = my(arr[0:mid])
            curr.right = my(arr[mid+1:])
            return curr
        return my(nums)

        