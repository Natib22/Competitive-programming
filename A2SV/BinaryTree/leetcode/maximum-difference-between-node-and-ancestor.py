# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        arr = [0]
        def my(root,mymax , mymin):
            if root:
                if abs(mymax - root.val) > arr[-1]:
                    arr[0] = abs(mymax - root.val)
                if abs(mymin - root.val) > arr[-1]:
                    arr[0] = abs(mymin - root.val)
                mymax = max(root.val ,mymax)
                mymin = min(root.val , mymin)
                my(root.left,mymax,mymin)
                my(root.right,mymax,mymin)
            else:
                return
        my(root,root.val,root.val)
        return arr[0]
                

        