class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0
        for num in nums:
            if num-1 not in nums:
                end = num+1
                while end in nums:
                    end += 1
                maxLen = max(maxLen, end-num)
        return maxLen
    
    
        """
        Approach 1 - Sort the array and check for consecutive element
        skip for duplicate elements
        initialise currLen and maxLen to 1 and update maxLen by maximum of maxLen and currLen
        if consecutive diff = 1 then currLen += 1 else currLen = 1
        return maxLen
        Time Complexity - O(NLogN)
        Space Complexity - O(1)
        """
        if not nums:
            return 0
        nums.sort()
        maxLen = 1
        currLen = 1
        for i in range(1, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]-nums[i-1] == 1:
                currLen +=  1 
            else:
                currLen = 1
            maxLen = max(currLen, maxLen)
        return maxLen