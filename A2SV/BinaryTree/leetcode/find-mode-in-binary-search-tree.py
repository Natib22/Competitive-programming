# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mymap = defaultdict(int)
        def my(root):
            if root:
                mymap[root.val] +=1
                my(root.left)
                my(root.right)
            else:
                return
        my(root)
        res = []
        curr = 0
        for i in mymap.values():
            curr = max(curr , i)
        for i , j in mymap.items():
            if j == curr:
                res.append(i)
        return res
        

        