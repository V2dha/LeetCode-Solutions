# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Approach - Using DFS Recursion
        Time Complexity - O(N)
        Space Complexity - O(N) Recursion Stack
        """
        if root == None or root == p or root == q:
            return root
        
        #Find p or q in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        #Find p or q in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        
        #If left and right both have p or q return root as it would be LCA
        if left and right:
            return root
        
        #return either if either of them is present
        return left if left else right
        