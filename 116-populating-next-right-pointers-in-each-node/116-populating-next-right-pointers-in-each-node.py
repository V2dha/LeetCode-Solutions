"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Approach - Using Level Order Traversal
        1. if not root return root
        2. Initialize a queue and add root and none in it
        3. go through the queue while it not empty
            a. pop the first inserted node
            b. if the node is not none
                i. set the node.next as first element of queue
                ii. if node.left exists and node.right exists append it to the queue
            c. if the node is none but len(queue) > 0
                i. then append none in queue
        """
        if not root:
            return root
        queue = []
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.pop(0)
            if node:
                node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if len(queue):
                    queue.append(None)
        return root