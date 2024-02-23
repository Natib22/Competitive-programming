# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        
        def my(root1 , root2):
            if root1 or root2:
                
                if root1 and root2:
                    root1.left = my(root1.left, root2.left)
                    root1.right = my(root1.right, root2.right)
                    root1.val+= root2.val
                    return root1
                    
                elif root2:
                    return root2
                
                else:
                    return root1
                
               
            else:
                return None
        if root1:
            my(root1,root2)
        else:
            return root2

            
            
        return root1

        