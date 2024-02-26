class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mymap = {}
        
        def dfs(node, col, row):
            if node:
                if col in mymap:
                    mymap[col].append((row, node.val))
                else:
                    mymap[col] = [(row, node.val)]
                
                dfs(node.left, col - 1, row + 1)
                dfs(node.right, col + 1, row + 1)
        
        dfs(root, 0, 0)
        
        res = []
        for col in sorted(mymap):
            column = []
            for row, val in sorted(mymap[col]):
                column.append(val)
            res.append(column)
        
        return res
