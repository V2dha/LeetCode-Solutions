class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum, osum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if csum >= 0:
                csum += nums[i]
            else:
                csum = nums[i]
            if csum > osum:
                osum = csum
        return osum