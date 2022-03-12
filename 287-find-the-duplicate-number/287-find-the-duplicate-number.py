class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Approach - Floyd's Cycle Detection Algorithm (index and value range)
        Similar to detect a loop in Linked List
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        