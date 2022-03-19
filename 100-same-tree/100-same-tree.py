# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach - 
        1.if both are empty return true -> if p is None and q is None then return True
        2.if one of them is empty return false -> if p is None or q is None then return False
        3. if value of root is not equal return false -> if p.val != q.val then return False
        4. check for the left subTree or child and right subTree or child
            leftTree = self.isSameTree(p.left, q.left)
            rightTree = self.isSameTree(p.right, q.right)
        5. if both leftTree and rightTree are True return True -> if leftTree and rightTree then return True
        6. else return False -> return False
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
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
        
        
        
        
        