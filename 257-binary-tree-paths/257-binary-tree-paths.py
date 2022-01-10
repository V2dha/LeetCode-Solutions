# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        s = ""
        def pathRec(root, s):
            if not root:
                return
            s += str(root.val)
            
            pathRec(root.left, s+'->')
            pathRec(root.right, s+'->')
            
            if not root.left and not root.right:
                self.ans.append(s)
            
        pathRec(root, s)
        return self.ans
            
            
            
        