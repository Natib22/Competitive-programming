# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def my(root , p , q):
            if root:
                if p.val < root.val  < q.val:
                    return root
                elif root.val== p.val or root.val ==q.val:
                    return root
                
                elif root.val < p.val:
                    return my(root.right , p , q)
                else:
                   return my(root.left , p ,q)
            else:

                return
        if p.val < q.val:
            return my(root, p , q)
        return my(root, q , p)
            
            
        