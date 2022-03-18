# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 2. Using Iteration
        1. Initialise stack, node = root and inorder list
        2. Initialise infinite loop -> while True
        3. if node then stack.append(node) and node = node.left
        4. else if not stack then break 
        5. Assign node = stack.pop() 
        6. Insert node.val in inorder list and node = node.right
        7. return inorder list
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
        stack = []
        node = root
        inorder = []
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack: 
                    break
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
        return inorder
        
        """
        Approach 1. Using Recursion
        1. Initialise empty list to store vals and then call solve function passing list and root
        2. Declare solve function with paramenters root and ele
        3. If not root -> return 
        4. Call solve function for left subtree -> solve(root.left, ele)
        5. Add root.val in elements -> ele.append(root.val)
        6. Call solve function for right subtree -> solve(root.right, ele)
        Time Complexity - O(N)
        Space Complexity - O(N) Recursion Stack
        """
        ele = []
        self.solve(root, ele)
        return ele
    
    def solve(self, root, ele):
        if not root:
            return 
        self.solve(root.left, ele)
        ele.append(root.val)
        self.solve(root.right, ele)
        