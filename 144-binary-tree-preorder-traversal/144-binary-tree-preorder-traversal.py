# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 2. Using Iteration and stack
        Same as inoder except add before appending to stack
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
        stack = []
        node = root
        preorder = []
        while True:
            if node:
                preorder.append(node.val)
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                node = node.right
        return preorder
        
        """
        Approach 1. Using Recursion
        1. if not root return
        2. preorder.append(root.val)
        3. solve(root.left) and solve(root.right)
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
        preorder = []
        self.solve(root, preorder)
        return preorder
    
    def solve(self, root, preorder):
        if not root:
            return 
        preorder.append(root.val)
        self.solve(root.left, preorder)
        self.solve(root.right, preorder)