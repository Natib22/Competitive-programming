# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def rev(arr):
            left = 0
            right = len(arr)-1
            while left < right:
                [arr[left] , arr[right]] = [arr[right] , arr[left]]
                left+=1
                right-=1
            return arr
        mymap = defaultdict(list)
        arr =[]
        def my(root,row):
            if root:
                mymap[row].append(root.val)
                my(root.left,row+1)
                my(root.right,row+1)
            else:
                return
        my(root,2)
  
        for key , value in mymap.items():
            if key % 2==1:
                arr.append(rev(value))
            else:
                arr.append(value)

        return arr

        
                
        