# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach - using a queue
        1. if not root return None
        2. Initialize a queue and levelList to store Levels
        3. insert root into queue
        4. go through the queue while it is not empty
            a. initialize a list level to store
            b. iterate through the queue
                i. pop the first inserted element
                ii. insert it into the level
                iii. append its left child and right child in the queue if they are not None
            c. insert level into levelList
        5. return levelList
        Time Complexity - O(N)
        Space Complexity - O(N)
        """        
        if not root:
            return []
        queue = deque()
        levelList = []
        queue.append(root)
        while len(queue):
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelList.append(level)
        return levelList
        
        