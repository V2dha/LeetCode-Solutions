class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev = nums[::-1]
        for i in range(1, len(nums)):
            if nums[i-1]!=0:
                nums[i]*=nums[i-1]
            if rev[i-1]!=0:
                rev[i]*=rev[i-1]
        return max(rev+nums)
            
            