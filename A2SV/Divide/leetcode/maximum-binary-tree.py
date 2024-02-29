# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for i in range(len(nums)):
            node = TreeNode(nums[i])
            if stack:
                if nums[i] < stack[-1].val:
                    stack[-1].right = node
                    
                else:
                    while stack and nums[i] > stack[-1].val:
                        node.left = stack.pop()
                    if stack:
                        stack[-1].right = node
            stack.append(node)
          
        return stack[0]

        