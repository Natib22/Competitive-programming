# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        arr = []
        def my(root):
            if root:
                my(root.left)
                arr.append(root.val)
                my(root.right)
            else:
                return
        my(root)

        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                return False 
        
        return True


                
        