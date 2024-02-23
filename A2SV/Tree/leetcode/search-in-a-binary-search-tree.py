# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def my(root,val):
            if root:
                if root.val == val:
                    return root
                if root.val < val:
                    return my(root.right,val)
                else:
                    return my(root.left,val)
            else:
                return
        
        return my(root,val)


        