class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxLen = 0
        currLen = 0
        for i in range(1, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]-nums[i-1] == 1:
                currLen +=  1 
            else:
                currLen = 0
            maxLen = max(currLen, maxLen)
        return maxLen+1