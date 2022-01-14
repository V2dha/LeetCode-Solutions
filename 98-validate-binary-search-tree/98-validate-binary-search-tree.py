# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Approach - Using Inorder Traversal
        Since inorder traversal traverses the BST in ascending order so it can be used to check the 
        validity of BST
        """
#         def inorder(root, elements):
#             if not root:
#                 return 
#             inorder(root.left, elements)
#             elements.append(root.val)
#             inorder(root.right, elements)
            
#         elements = []
#         inorder(root, elements)
#         for i in range(1, len(elements)):
#             if elements[i-1] >= elements[i]:
#                 return False
#         return True
        """
        Second Approach - Recursive
        """
        self.answer=True
        
        def dfs(root, left, right):
            if root:
                if left >= root.val or root.val >= right:
                    self.answer = False
                    return
                dfs(root.left, left, root.val)
                dfs(root.right, root.val, right)
                
        dfs(root, float("-inf"), float('inf'))
        return self.answer
        