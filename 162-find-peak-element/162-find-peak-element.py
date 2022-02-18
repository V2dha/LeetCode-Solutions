class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = nums[0]
        index = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i] and nums[i] > peak:
                peak = nums[i]
                index = i
        return index
            
                
        