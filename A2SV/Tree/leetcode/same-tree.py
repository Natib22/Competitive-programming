# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr=[True]
        def my( p , q):
            
            if p and q:
                if p.val == q.val:
                    my(p.left,q.left)
                    my(p.right,q.right)
                else:
                    arr[0] = False
                    print(p.val , q.val)
                 
                    return
            elif p and not q:
                arr[0] = False
                
            elif q and not p :
                arr[0] = False
                
            
            return None
        my(p,q)
        return arr[0]


        