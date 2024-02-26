# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def my(root,num):
            if root:
                num+= str(root.val)
                if root.left:
                    my(root.left,num)
                if root.right:
                    my(root.right,num)
                if not root.right and not root.left:
                    arr.append(num)
            else:
                return
        my(root,"")
        ans = 0
        for i in arr:
            ans+= int(i)
        return ans

        