class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        d = -1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                d = nums[i]
                
        return d 
        