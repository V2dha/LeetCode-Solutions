class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        csum, ssum = 0, 0
        osum = 0
        for i in range(len(nums)):
            csum = csum + nums[i]
            ssum = ssum + nums[i]
            osum = max(osum, csum, abs(ssum))
            if (csum < 0):
                csum = 0
            if (ssum > 0):
                ssum = 0
        return osum