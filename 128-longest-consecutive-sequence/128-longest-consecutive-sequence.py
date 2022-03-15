class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Approach - Using set
        1. First turn the input into a set of numbers. That takes O(n) and O(1) for searching
        2. If the number x is the start of a streak (i.e., x-1 is not in the set), 
        then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set
        3. The length of the streak is then simply y-x and we update our global best with that. 
        Since we check each streak only once, this is overall O(n)
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
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