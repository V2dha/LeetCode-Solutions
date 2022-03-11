class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        osum = nums[0]
        for i in range(1, len(nums)):
            if csum < 0:
                csum = nums[i]
            else:
                csum += nums[i]
            osum = max(csum, osum)
        return osum
        
        