class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Approach - Kadane's Algorithm
        1. initialise current sum and overall sum to first value 
        2. iterate from 1 to end, if csum >= 0 add nums[i] else initialise csum = nums[i]
        3. update maximum of osum and csum
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        csum = nums[0]
        osum = nums[0]
        for i in range(1, len(nums)):
            if csum < 0:
                csum = nums[i]
            else:
                csum += nums[i]
            osum = max(csum, osum)
        return osum
        
        