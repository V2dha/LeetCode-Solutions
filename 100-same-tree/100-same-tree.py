# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are empty return true
        if p is None and q is None:
            return True
        # if one of them is empty return false
        if p is None or q is None:
            return False
        # if value of root is not equal return false
        if p.val != q.val:
            return False
        # check for the left subTree or child and right subTree or child
        leftTree = self.isSameTree(p.left, q.left)
        rightTree = self.isSameTree(p.right, q.right)
        # if both leftTree and rightTree are True return True
        if leftTree and rightTree:
            return True
        # else return False
        return False
        
        
        
        
        