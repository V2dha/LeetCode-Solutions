class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            currentpos = nums[i] - 1
            while 1 <= nums[i] <= n and nums[i] != nums[currentpos]:
                nums[i], nums[currentpos] = nums[currentpos], nums[i]
                currentpos = nums[i] - 1
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
        