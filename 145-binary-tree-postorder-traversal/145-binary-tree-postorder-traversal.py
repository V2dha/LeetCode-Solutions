# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 2. Using stack 
        """
        res = []
        stack = []
        if not root:
            return res
        node = root
        while True:
            if node:
                res.append(node.val)
                stack.append(node)
                node = node.right
            else:
                if not stack:
                    break
                node = stack.pop()
                node = node.left
        return res[::-1]
            
        
        
        """
        Approach 1.Using Recursion
        1. Left subtree
        2. Right subtree
        3. Root node
        Time Complexity - O(N)
        Space Complexity - O(N) (Recursion Stack)
        """
        ele = []
        def postOrder(root, ele):
            if not root:
                return
            postOrder(root.left, ele)
            postOrder(root.right, ele)
            ele.append(root.val)
        postOrder(root, ele)
        return ele
            
        