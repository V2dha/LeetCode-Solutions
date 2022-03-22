# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 1.Using Recursion
        1. Left subtree
        2. Right subtree
        3. Root node
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
            
        