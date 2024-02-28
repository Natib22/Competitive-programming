# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        num = root.val
        if num >=low and num<=high:
            sum= num
        else:
            sum = 0
        return sum + self.rangeSumBST(root.left,low,high)+ self.rangeSumBST(root.right,low,high)
