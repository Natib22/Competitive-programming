# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def my(root):
            if root:
                my(root.left)

                arr.append(root.val)
                my(root.right)
            else:
                return
        my(root)
       
        return arr[k-1]
        